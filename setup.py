# File: setup.py
from setuptools import setup, find_packages

setup(
    name='autoheal-agent',  # Replace with your package name
    version='0.1.0',  # Replace with your package version
    packages=find_packages(),  # Automatically find packages in the current directory
    install_requires=[
        'pyyaml',
        ],
    entry_points={
        'console_scripts': [
            'autoheal-agent = agent.main:main',  # Replace with your main function
        ],
    },
    author='Sudipta Chatterjee',  
    description='A autoheal agent that runs automated fixes on CI/CD pipelies.', 
    include_package_data=True,
)