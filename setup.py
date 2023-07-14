from setuptools import setup, find_packages

setup(
    name='easy-env',
    version='1.0.0',
    author='Antoine PINTO',
    author_email='antoine.pinto1@outlook.fr',
    description='Easy-to-use functionality for managing files in different environments',
    long_description='Easy Environment is a Python tool that provides easy-to-use functionality for managing files and data in different environments. It offers a class called Environment that simplifies file operations on the local disk and cloud services such as Google Cloud (Google Cloud Storage and Big Query) or SharePoint.',
    packages=find_packages(),
    install_requires=[
    ],
)