from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Yeh line change karo
        requirements = [req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name='fault_detection',  # Space ki jagah underscore use karo
    version='0.0.1',
    author_email='ahmedrajakhan56@gmail.com',
    author='ahmed raja khan',
    install_requires=get_requirements('requirements.txt'),  # Yeh line correct karo
    packages=find_packages()
)