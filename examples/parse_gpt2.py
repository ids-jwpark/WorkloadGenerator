from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch.onnx
import torch
import onnx
import numpy as np
import onnxruntime as ort
from workload_generator import parse_onnx, write_csv

# Load the pretrained model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Example usage
input_text = "Hello, how are you?"
input_ids = tokenizer.encode(input_text, return_tensors="pt")
output = model.generate(input_ids)
decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)

print(decoded_output)


# Set the path for saving the ONNX file
onnx_file_path = "tests/model.onnx"

# Set the input tensor
input_ids = torch.tensor([[15496, 11, 703, 389, 345, 30]])

# Export the model to ONNX
torch.onnx.export(model, input_ids, onnx_file_path)

# Load the ONNX model
onnx_model = onnx.load("tests/model.onnx")

# Parse the ONNX model
parsed_model = parse_onnx(onnx_model)

# Write the parsed model to a CSV file
write_csv(parsed_model, "tests/model.csv")