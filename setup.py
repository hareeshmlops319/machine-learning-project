''' The setup.py file is an essential part of packaging and distributing python projects. It is used by setup tools script for the network-security package. '''
from setuptools import setup, find_packages

def  get_requirements()->list[str]:
    ''' This function will return the list of requirements '''
    try:
        with open('requirements.txt', 'r') as file:
             # Read the requirments from the file.
             lines=file.readlines()
             # proces each line
             requirements_list:list[str]=[]
             for line in lines:
                 requirment = line.strip()
                 if requirment and requirment!= '-e .':
                     requirements_list.append(requirment)
    except FileNotFoundError:
        print("Requirments file not found")
    return requirements_list

setup(
    name='network-security',
    version='0.0.1',
    author='Hareesh Yalamasetty',
    packages=find_packages(),
    install_requires=get_requirements(),
    description='A package for network security analysis and phishing detection',       
)
                     
                     
