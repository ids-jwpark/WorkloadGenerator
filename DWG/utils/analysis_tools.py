import onnx

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



