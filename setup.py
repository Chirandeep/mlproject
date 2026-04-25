from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e."

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns the list of requirements
    """
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newline characters
        requirements = [req.strip() for req in requirements]

        # Remove '-e .'
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='chirandeep',
    author_email='chirandeeppp@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)