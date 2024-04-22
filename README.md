# Workload Generator

## Overview
The Workload Generator is a project that accepts a PyTorch model and a test input set. It generates an ONNX file and analyzes the types of operators inside the ONNX. It also provides approximations for MAC counts, the number of parameters, input/output sizes, and more in a report object.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/idslab-skku/WorkloadGenerator.git
    ```

2. Create a new conda environment and activate it:
    ```bash
    conda env create -f environment.yml
    conda activate workload-generator
    ```


## Usage
1. Import the necessary modules:
    ```python
    import torch
    import onnx
    from WOrkloadGenerator import WorkloadGenerator
    ```

2. Load your PyTorch model and test input set:
    ```python
    model = torch.load('path/to/your/model.pth')
    test_input = torch.load('path/to/your/test_input.pth')
    ```

3. Generate the ONNX file:
    ```python
    generator = WorkloadGenerator(model)
    onnx_file = generator.generate_onnx('path/to/save/onnx/model.onnx')
    ```

4. Analyze the ONNX file and generate the report:
    ```python
    report = generator.analyze_onnx(onnx_file)
    ```

5. Access the information in the report object:
    ```python
    mac_counts = report.mac_counts
    num_parameters = report.num_parameters
    input_size = report.input_size
    output_size = report.output_size
    # ... and more
    ```


## License
This project is licensed under the [MIT License](LICENSE).