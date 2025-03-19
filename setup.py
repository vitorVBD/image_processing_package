from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    page_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Vitor Bittencourt",
    description="A package to process images",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vitorVBD/image_processing_package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)