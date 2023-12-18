"""
This setup.py file contains configurations for installing and setting up the project.
"""

from setuptools import find_packages, setup


def get_requirements():
    """
    This function will return a list of requirements
    """
    with open("requirements.txt", encoding='utf-8') as f:
        lines = f.read()

    list_packages = lines.split('\n')

    return list_packages


setup(
    name="finance",
    version="0.0.1",
    author="Prathamesh Mohite",
    author_email="prathamesh.mohite96@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
