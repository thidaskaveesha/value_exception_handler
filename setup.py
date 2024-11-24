from setuptools import setup, find_packages

setup(
    name="value-error-exception-handler",  
    version="0.1.0",  
    author="Thidas Senavirathna",
    author_email="thidaskaveesha@gmail.com",
    description="A utility for handling user input validation and exceptions in Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/value-error-exception-handler",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
