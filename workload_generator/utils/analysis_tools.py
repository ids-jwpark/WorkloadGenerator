import onnx
from typing import NamedTuple, Optional, Dict
from workload_generator import ParsedModel
import torch

def write_csv(pmodel_dict: Dict[str, ParsedModel], filename) -> None:
    """
    Write the parsed model to a csv file.
    If the pmodel contains both GEMM types and CONV types,
    the csv file will be written twice: one for GEMM and one for CONV.
    the names of file will be {write_file}_gemm.csv and {write_file_conv}.csv
    """
    # Drop ".csv" from the writefile name if it exists
    if filename.endswith(".csv"):
        filename = filename[:-4]

    # First iterate through the keys of the dictionary
    keys = pmodel_dict.keys()
    # Check if the dictionary contains both GEMM and CONV types
    # Extract the op_type from all keys
    op_types = [pmodel_dict[p].op_type for p in keys]
    mix_gemm_and_conv = "Gemm" in op_types and "Conv" in op_types
    # Extract op type that is neither gemm, conv, nor matmul
    other_ops = [pmodel_dict[p].op_type for p in keys if pmodel_dict[p].op_type not in ["Gemm", "Conv", "MatMul"]]
    # Generate warnings for other_ops
    if other_ops:
        print(f"Warning: The following op types are not supported: {set(other_ops)}")
    # If there are both GEMM and CONV types, write two separate csv files
    if mix_gemm_and_conv:
        write_csv_gemm(pmodel_dict, filename + "_gemm.csv")
        write_csv_conv(pmodel_dict, filename + "_conv.csv")
    elif "Gemm" in op_types:
        write_csv_gemm(pmodel_dict, filename + ".csv")
    
    
def write_csv_gemm(pmodel_dict: Dict[str,ParsedModel], filename, unique_only=True) -> None:
    pmodel_dict = {k: v for k,v in pmodel_dict.items() if v.op_type == 'Gemm' or v.op_type == 'MatMul'}
    # GEMM lines should indictate:
    # Name, M, N, K, i_wordsize, f_wordsize, o_wordsize
    duplicates = set()
    with open(filename, "w") as f:
        f.write("Name,M,N,K,i_wordsize,f_wordsize,o_wordsize,\n")
        for name, pmodel in pmodel_dict.items():
            # Sanity check: Verify that M = input_shapes[0][0] = output_shapes[0][0], 
            # N = input_shapes[0][1] = input_shapes[1][0], K = output_shapes[0][1] = input_shapes[1][1]
            M = pmodel.input_shapes[0][0]
            N = pmodel.input_shapes[0][1]
            K = pmodel.input_shapes[1][1]
            assert M == pmodel.output_shapes[0][0], f"M != output_shapes[0][0] at {name}"
            assert N == pmodel.input_shapes[1][0], f"N != input_shapes[1][0] at {name}"
            assert K == pmodel.output_shapes[0][1], f"K != output_shapes[0][1] at {name}"
            # Check word sizes: f_wordsize is 0.5 if param_shapes is not empty
            f_wordsize = 0.5 if pmodel.param_shapes else 2
            i_wordsize = 2
            o_wordsize = 2
            if unique_only and (M, N, K, i_wordsize, f_wordsize, o_wordsize) in duplicates:
                print(f"Duplicate found: {name}")
                continue
            duplicates.add((M, N, K, i_wordsize, f_wordsize, o_wordsize))
            f.write(f"{name},{M},{N},{K},{i_wordsize},{f_wordsize},{o_wordsize},\n")
    return

def write_csv_conv(pmodel_dict: Dict[str,ParsedModel], filename, unique_only=True):
    raise NotImplementedError("write_csv_conv is not implemented yet.")
    return

# Typing: pmodel is a dict with str as key, ParsedModel as Value

# A torch hook function that will be called when the forward pass is executed
# It will store the input data of the layer.
def store_input_hook(module, input, output):
    module.input = input

# Example usage:
# model = torch.nn.Linear(10, 5)
# model.register_forward_hook(store_input_hook)

