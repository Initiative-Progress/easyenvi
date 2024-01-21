import pytest
from utils import load_envi

envi = load_envi()

def test_bq_write():
    dataset = envi.local.load('rsc/inputs/test.parquet')
    envi.gcloud.BQ.write(dataset, 'mydata.mytable')

def test_bq_append():
    dataset = envi.local.load('rsc/inputs/test.parquet')
    envi.gcloud.BQ.append(dataset, 'mydata.mytable')

def test_bq_query():
    query = """
    SELECT *
    FROM mydata.mytable
    WHERE Age > 50
    """

    new_dataset = envi.gcloud.BQ.query(query).to_dataframe()

    # TO DO : check if dataset corresponds