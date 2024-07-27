import pytest

@pytest.mark.parametrize("gcs_format", [
    "csv", "docx", "json", "md", "parquet", "pdf", "pptx",
    "sql", "toml", "txt", "xlsx", "xml", "yaml", "yml"
])
def test_gcs_load_save(envi, gcs_format):

    gcs_path = f"test.{gcs_format}"

    # Google Cloud Storage operations
    test = envi.gcloud.GCS.load(gcs_path)
    envi.gcloud.GCS.save(test, gcs_path)