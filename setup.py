import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='workload_generator',
    version='0.0.1',
    description='Workload Generator',
    long_description=README,
    long_description_content_type="text/markdown",
    author='jeongwoo park',
    author_email='jeffjw@skku.edu',
    maintainer='idslab',
    maintainer_email='jeffjw@skku.edu',
    packages=find_packages(),
    include_package_data=False,                                 # The include_package_data argument controls whether non-code files are copied when your package is installed
    install_requires=["onnx", "onnxruntime", "numpy"],
    classifiers=[
        'Development Status :: 0 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering'
    ]
)
