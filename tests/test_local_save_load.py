import pytest


@pytest.mark.parametrize("local_format", [
    "csv", "docx", "jpg", "json", "md", "parquet", "pdf", "png", "pptx",
    "sql", "toml", "txt", "xlsx", "xml", "yaml", "yml"
])
def test_local_load_save(envi, local_format):

    # Load the test file
    test = envi.local.load(f"tests/rsc/inputs/test.{local_format}")
    
    # Save the test file
    output_path = f"tests/rsc/outputs/test.{local_format}"
    envi.local.save(test, output_path)

@pytest.mark.parametrize("local_format", [
    "csv", "docx", "jpg", "json", "md", "parquet", "pdf", "png", "pptx",
    "sql", "toml", "txt", "xlsx", "xml", "yaml", "yml"
])
def test_local_load_save_file_method(local_format):

    from easyenvi import file

    # Load the test file
    test = file.load(f"tests/rsc/inputs/test.{local_format}")
    
    # Save the test file
    output_path = f"tests/rsc/outputs/test.{local_format}"
    file.save(test, output_path)