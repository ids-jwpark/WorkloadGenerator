import onnx
from typing import NamedTuple, Optional, Dict


def count_operators(model):
    """
    Count the number of operators in an ONNX model.
    """
    #model = onnx.load(onnx_operator)
    count = {}
    for node in model.graph.node:
        if node.op_type in count:
            count[node.op_type] += 1
        else:
            count[node.op_type] = 1
    return count

def count_parameters(onnx_operator):
    """
    Count the number of parameters in an ONNX model.
    """
    model = onnx.load(onnx_operator)
    param_count = 0
    num_params = 0
    for node in model.graph.initializer:
        # Count the number of parameters & its size in each node
        param_count += 1
        # Get the size of the parameter, also account for data type
        num_params += node.raw_data.size / node.raw_data.itemsize


class ParsedModel(NamedTuple):
    """
    Parsed Model: Required: op_type, input_shapes, output_shapes, macs
    Optional: attributes, param_shapes
    op_type: str, just the type of operation
    input_shapes: input shapes of the operation, list of int tuples
    output_shapes: output shapes of the operation, list of int tuples
    macs: number of Multiply-Accumulate operations
    attributes: optional attributes of the operation, dictionary
    param_shapes: optional parameter shapes of the operation, list of int tuples
    """
    op_type: str
    input_shapes: list
    output_shapes: list
    macs: int
    attribute: Optional[list]
    param_shapes: Optional[list] = []

def reformat_name(tensor_name):
    """
    Reformat tensor name if it starts with "/", so that all "/" are changed to "." 
    and the first "." is removed.
    """
    if tensor_name.startswith("/"):
        tensor_name = tensor_name[1:]
    return tensor_name.replace("/", ".")


def parse_convnode(node, value_dict, param_dict):
    """
    Parse Convolutional node to include input and output shapes.
    Count MACs for Convolutional layers.
    """
    # Get the input size
    input_name = reformat_name(node.input[0])
    input_shape = value_dict[input_name].type.tensor_type.shape.dim
    input_channels = input_shape[1].dim_value
    # Get the output size
    output_name = reformat_name(node.output[0])
    output_shape = value_dict[output_name].type.tensor_type.shape.dim
    output_channels = output_shape[1].dim_value
    # Get the kernel size
    kernel_name = reformat_name(node.input[1])
    kernel_shape = param_dict[kernel_name].dims
    kernel_size = kernel_shape[-2:]
    # Also check for bias
    bias_shape = None
    if len(node.input) == 3:
        bias_name = reformat_name(node.input[2])
        bias_shape = param_dict[bias_name].dims
        bias_size = bias_shape[0]
    # Get the number of MACs
    macs = np.prod(kernel_size) * input_channels * output_channels * np.prod(output_shape[2:]) + (0 if bias_shape is None else output_channels * np.prod(output_shape[2:]))
    # Create ParsedModel object.
    # First map input_shape and output_shape to a single element list 
    if bias_shape is not None:
        input_shape = [tuple([d.dim_value for d in input_shape]), tuple([d for d in kernel_shape]), tuple([d for d in bias_shape])]
    else:
        input_shape = [tuple([d.dim_value for d in input_shape]), tuple([d for d in kernel_shape])]
    output_shape = [tuple([d.dim_value for d in output_shape])]
    # Create param_shapes
    param_shapes = [tuple([d for d in kernel_shape])]
    return ParsedModel(node.op_type, input_shape, output_shape, macs, attribute=node.attribute, param_shapes=param_shapes)

def parse_gemmnode(node, value_dict, param_dict):
    """
    Parse Gemm node to include input and output shapes.
    Count MACs for Gemm operations.
    """
    param_shapes = []
    # Get the input size for #0
    i1_name = reformat_name(node.input[0])
    # Check if i1 in param dict
    if i1_name in param_dict:
        param_shapes.append(tuple([d for d in param_dict[i1_name].dims]))
        i1_channels = param_dict[i1_name].dims[0]
        internal_channels = param_dict[i1_name].dims[1]
    else:
        i1_shape = value_dict[i1_name].type.tensor_type.shape.dim
        internal_channels = i1_shape[1].dim_value
        i1_channels = i1_shape[0].dim_value
    # Get the input size for #1
    i2_name = reformat_name(node.input[1])
    # Check if i2 in param dict
    if i2_name in param_dict:
        param_shapes.append(tuple([d for d in param_dict[i2_name].dims]))
        i2_channels = param_dict[i2_name].dims[1]
    else:
        i2_shape = value_dict[i2_name].type.tensor_type.shape.dim
        i2_channels = i2_shape[1].dim_value
    
    # Check if bias is present
    bias_shape = None
    if len(node.input) == 3:
        bias_name = reformat_name(node.input[2])
        bias_shape = param_dict[bias_name].dims
        bias_size = bias_shape[0]
        param_shapes.append(tuple([d for d in bias_shape]))
    # Get the number of MACs
    macs = i1_channels * internal_channels * i2_channels
    if bias_shape is not None:
        input_shapes = [tuple([i1_channels, internal_channels]), tuple([internal_channels, i2_channels]), tuple([i2_channels])]
    else:
        input_shapes = [tuple([i1_channels, internal_channels]), tuple([internal_channels, i2_channels])]
    return ParsedModel(node.op_type, input_shapes, [tuple([i1_channels, i2_channels])], macs, attribute=node.attribute, param_shapes=param_shapes)

def parse_onnx(onnx_model):
    """
    Parse ONNX model file to include input and output shapes.
    Cout MACs for Convolutional layers, Gemm, and Matmul operations.
    """
    # First check if op type is supported
    supported_ops = ["Conv", "MatMul", "Gemm"]
    parsed_model = {}
    # Parsed model should have the following fixed fields in NamedTuple:
    # op_type, input_shapes, output_shapes, macs, attributes (optional), param_shapes (optional, only if in graph.initializer)
    warning_issued=False
    # If onnx_model's value info is empty list, generate with shape inference
    if not onnx_model.graph.value_info:
        onnx_model = onnx.shape_inference.infer_shapes(onnx_model)
    value_info = onnx_model.graph.value_info
    value_dict = {reformat_name(v.name): v for v in value_info}

    # Also include the output of graph.node to the value_dict
    for out in onnx_model.graph.output:
        value_dict[reformat_name(out.name)] = out

    param_info = onnx_model.graph.initializer
    param_dict = {p.name: p for p in param_info}
    other_ops = {}
    for node in onnx_model.graph.node:
        # Check if the node is supported
        if not any([op_type in node.op_type for op_type in supported_ops]):
            if node.op_type in other_ops:
                other_ops[node.op_type].append(node.name)
            else:
                other_ops[node.op_type] = [node.name]
            if not warning_issued:
                print(f"Warning: {node.op_type} is not supported.")
                warning_issued = True


        # Count MACs for Conv
        if "Conv" in node.op_type:
            parsed_model[reformat_name(node.name)] = parse_convnode(node, value_dict, param_dict)
        # Count MACs for Gemm
        elif "Gemm" in node.op_type:
            parsed_model[reformat_name(node.name)] = parse_gemmnode(node, value_dict, param_dict)
        # Count MACs for MatMul
        elif "MatMul" in node.op_type:
            parsed_model[reformat_name(node.name)] = parse_gemmnode(node, value_dict, param_dict)
        
        # Only Parsing Conv, GEMM, Matmul for now. Add more as needed.
    return parsed_model, other_ops
