from setuptools import find_packages,setup
from typing import List

requirement_file_name='requirements.txt'

REMOVE_PACKAGE='-e .'

def get_requirements()->list[str]:
    requirement_list=[]
    with open(requirement_file_name) as requirement_file: 
        requirement_list=requirement_file.readlines()
        requirement_list=[requirement_name.replace('\n','') for requirement_name in requirement_list]

    if REMOVE_PACKAGE in requirement_list:
        requirement_list.remove(REMOVE_PACKAGE)
    return requirement_list

setup(
    name='Diabates Classification ML project',
    version='1.0',
    description='Data Science Pipeline',
    author='Gautam',
    author_email='gautammahtoaiie31aii.ac.in@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
) 