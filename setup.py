from setuptools import setup , find_packages
import os
from typing import List

def get_requirenment(file_path:str)->List[str]:
    requirenment=[]
    with open(file_path) as file_obj:
        requirenment=file_obj.readlines()
        requirenment=[req.replace("\n","") for req in requirenment]
        return requirenment



setup(
    name='git',
    author='sumit',
    author_email='sumitnsawant822@gmail.com',
    description='setting up file',
    packages=find_packages(),
    version="0.1.0",
    install_requires=get_requirenment('requirenment.txt')
    )