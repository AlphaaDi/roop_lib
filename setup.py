from setuptools import setup, find_packages

setup(
    name="roop",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'onnxruntime',
        'numpy',
        'opencv-python',
        'scikit-video',
        'munch',
    ],
)