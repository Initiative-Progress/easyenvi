import pytest
from utils import load_envi

envi = load_envi()

def test_sharepoint_download():
    envi.sharepoint.download(
        input_path="/Documents partages/knowledge/Départ.txt",
        output_path="rsc/outputs/Départ.txt"
        )
    
def test_sharepoint_list_files():
    envi.sharepoint.list_files(
        folder="Documents partages/knowledge"
        )

def test_sharepoint_upload():
    envi.sharepoint.upload(
        input_path="rsc/inputs/test.csv",
        output_path="Documents partages/knowledge/test.csv"
        )
    
def test_sharepoint_delete():
    envi.sharepoint.delete_file(
        file_path="/Documents partages/knowledge/test.csv"
    )