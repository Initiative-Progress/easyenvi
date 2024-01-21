import pytest
from utils import load_envi
from easyenvi import file

envi = load_envi()

@pytest.mark.parametrize("local_format", [
    'csv', 'docx', 'jpg', 'json', 'md', 'parquet', 'pdf', 'png', 'pptx',
    'sql', 'toml', 'txt', 'xlsx', 'xml', 'yaml', 'yml'
])
def test_local_load_save(local_format):
    # Load the test file
    test = envi.local.load(f'rsc/inputs/test.{local_format}')
    
    # Save the test file
    output_path = f'rsc/outputs/test.{local_format}'
    envi.local.save(test, output_path)
    
    # TO DO : Assert the file was saved correctly

@pytest.mark.parametrize("local_format", [
    'csv', 'docx', 'jpg', 'json', 'md', 'parquet', 'pdf', 'png', 'pptx',
    'sql', 'toml', 'txt', 'xlsx', 'xml', 'yaml', 'yml'
])
def test_local_load_save_file_method(local_format):
    # Load the test file
    test = file.load(f'rsc/inputs/test.{local_format}')
    
    # Save the test file
    output_path = f'rsc/outputs/test.{local_format}'
    file.save(test, output_path)
    
    # TO DO : Assert the file was saved correctly

@pytest.mark.parametrize("gcs_format", [
    'csv', 'docx', 'json', 'md', 'parquet', 'pdf', 'pptx',
    'sql', 'toml', 'txt', 'xlsx', 'xml', 'yaml', 'yml'
])
def test_gcs_load_save(gcs_format):

    gcs_path = f'test.{gcs_format}'

    # Google Cloud Storage operations
    test = envi.gcloud.GCS.load(gcs_path)
    envi.gcloud.GCS.save(test, gcs_path)