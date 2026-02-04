from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = "-e ."


def get_requirements(filename: str) -> List[str]:
    '''
    this function is used to get the requirements from a requirements file
    '''
    requirements = []
    with open(filename) as f:
        requirements = f.readlines()
        # Fixed the indentation below
        requirements = [req.replace("\n", "") for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Saransh',
    author_email='saranshoffice@gmail.com',
    packages=find_packages(),
    # Removed the duplicate manual list and kept the function call
    install_requires=get_requirements('requirements.txt'),
    python_requires='>=3.6'
)