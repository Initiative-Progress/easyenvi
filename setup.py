with open("README.md", "r") as f:
    long_description = f.read()

from setuptools import setup, find_packages

setup(
    name='easyenvi',
    version='1.0.7',
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
        "db-dtypes>=0.3.0",
        "fsspec>=2023.1.0",
        "gcsfs>=2023.1.0",
        "google-cloud-bigquery>=3.0.0",
        "google-cloud-storage>=2.0.0",
        "Office365-REST-Python-Client>=2.5.4",
        "openpyxl>=3.0.7",
        "pandas>=1.3.5",
        "pillow>=7.0.0",
        "pyarrow>=3.0.0",
        "PyPDF2>=2.5.0",
        "python-docx>=0.8.0",
        "python-pptx>=0.6.0",
        "pyyaml>=5.1",
        "toml>=0.9.0"
    ],
    python_requires='>=3.7'
)