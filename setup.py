with open("README.md", "r") as f:
    long_description = f.read()

from setuptools import setup, find_packages

setup(
    name='easyenvi',
    version='1.0.6',
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
    keywords=["file-manager", "easy-to-use", "environment", "cloud",
              "gcp", "sharepoint"],
    packages=find_packages(),
    install_requires=[
        "db-dtypes>=1.2.0",
        "fsspec>=2023.1.0",
        "gcsfs>=2023.1.0",
        "google-cloud-bigquery>=3.14.1",
        "google-cloud-storage>=2.14.0",
        "Office365-REST-Python-Client>=2.5.4",
        "openpyxl>=3.1.2",
        "pandas>=1.3.5",
        "pillow>=9.5.0",
        "pyarrow>=12.0.1",
        "PyPDF2>=3.0.1",
        "python-docx>=1.1.0",
        "python-pptx>=0.6.23",
        "pyyaml>=6.0.1",
        "toml>=0.10.2"
    ],
    python_requires='>=3.7'
)