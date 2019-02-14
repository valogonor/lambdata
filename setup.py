#!/user/bin/env python
''' Package setup/installation and metadata for lambdata
'''

import setuptools

REQUIRED = [
    "sklearn",
    "pandas"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="lambdata-valogonor",
    version="0.0.3",
    author="valogonor",
    description="A collection of Data Science helper functions",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/valogonor/lambdata",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)