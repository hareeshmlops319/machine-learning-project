''' The setup.py file is an essential part of packaging and distributing python projects.
It is used by setuptools for the Ml-Project package. '''

from setuptools import setup, find_packages
from typing import List


def get_requirements() -> List[str]:
    '''This function returns the list of requirements'''

    requirements_list: List[str] = []

    try:
        with open("requirements.txt", "r") as file:
            for line in file:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirements_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements_list


setup(
    name="ml-project",
    version="0.0.1",
    author="Hareesh Yalamasetty",
    author_email="hareesh.yalamasetty1@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
    description="A package for network security analysis and phishing detection",
)
