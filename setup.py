with open("README.md", "r") as f:
    long_description = f.read()

from setuptools import setup, find_packages

setup(
    name='easyenvi',
    version='1.0.4',
    description='Easy-to-use functionality for managing files and data in different environments',
    author='Antoine PINTO',
    author_email='antoine.pinto1@outlook.fr',
    license='MIT',
    license_file='LICENSE',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/AntoinePinto/easyenvi',
    project_urls={
        'Documentation': 'https://antoinepinto.gitbook.io/easyenvi/',
        'Source Code': 'https://github.com/AntoinePinto/easyenvi',
    },
    packages=find_packages(),
    install_requires=[
    ],
)