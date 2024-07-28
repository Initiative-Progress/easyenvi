import re

requirements = {
    "db-dtypes": "db-dtypes>=0.3.0",
    "gcsfs": "gcsfs>=2023.1.0",
    "google": "google-cloud-bigquery>=3.0.0 google-cloud-storage>=2.0.0",
    "office365": "Office365-REST-Python-Client>=2.5.4",
    "openpyxl": "openpyxl>=3.0.7",
    "pandas": "pandas>=1.3.5",
    "PIL": "pillow>=7.0.0",
    "pyarrow": "pyarrow>=3.0.0",
    "PyPDF2": "PyPDF2>=2.5.0",
    "docx": "python-docx>=0.8.0",
    "pptx": "python-pptx>=0.6.0",
    "yaml": "pyyaml>=5.1",
    "toml": "toml>=0.9.0"
}

def get_missing_module(error_message: str):
    pattern = r"No module named '(.*?)'"
    match = re.search(pattern, str(error_message))
    missing_module = match.group(1)

    return missing_module

def missing_module_error_handler(func):

    def wrapper(*args,  **kwargs):

        try:
            output = func(*args, **kwargs)
        except ModuleNotFoundError as e:
            missing_module = get_missing_module(e)
            if missing_module not in requirements:
                raise ModuleNotFoundError(f"No module named '{missing_module}'.")
            else:
                raise ModuleNotFoundError(
                    f"No module named '{missing_module}'. Please install it with `pip install {requirements[missing_module]}`"
                ) from None
        
        return output

    return wrapper