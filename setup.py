#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
setup.py

A basic setup script for packaging or distributing your Python project.
To build and install locally:
    python setup.py install
Or to package for PyPI:
    python setup.py sdist bdist_wheel
"""

import os
from setuptools import setup, find_packages

def read_file(fname):
    """Utility function to read a file's contents."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="my_predictive_modeling_project",  # Replace with your project name
    version="0.1.0",
    author="Your Name",
    author_email="you@example.com",
    description="Predictive modeling framework for dynamic morphology and stimulus-informed design.",
    long_description=read_file("README.md"),  # Assumes you have a top-level README.md
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/my-predictive-modeling-project",  # Replace with your repo URL
    packages=find_packages(where=".", exclude=["tests", "tests.*"]),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        # Add other dependencies listed in requirements.txt if you want them automatically installed
    ],
    python_requires=">=3.7",  # Specify minimum Python version if necessary
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Change license as needed
        "Operating System :: OS Independent",
    ],
    # If you have console scripts:
    entry_points={
        "console_scripts": [
            # Example: "dme_run = src.main:main"
        ],
    },
)
