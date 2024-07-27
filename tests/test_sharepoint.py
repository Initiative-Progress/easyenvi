def test_sharepoint_download(envi):
    envi.sharepoint.download(
        input_path="/Documents partages/knowledge/Départ.txt",
        output_path="tests/rsc/outputs/Départ.txt"
        )

def test_sharepoint_list_files(envi):
    envi.sharepoint.list_files(
        folder="Documents partages/knowledge"
        )

def test_sharepoint_upload(envi):
    envi.sharepoint.upload(
        input_path="tests/rsc/inputs/test.csv",
        output_path="Documents partages/knowledge/test.csv"
        )
    
def test_sharepoint_delete(envi):
    envi.sharepoint.delete_file(
        file_path="/Documents partages/knowledge/test.csv"
    )