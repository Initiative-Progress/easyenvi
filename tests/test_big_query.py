def test_bq_write(envi):
    dataset = envi.local.load("tests/rsc/inputs/test.parquet")
    envi.gcloud.BQ.write(dataset, "mydata.mytable")

def test_bq_append(envi):
    dataset = envi.local.load("tests/rsc/inputs/test.parquet")
    envi.gcloud.BQ.append(dataset, "mydata.mytable")

def test_bq_query(envi):
    query = """
    SELECT *
    FROM mydata.mytable
    WHERE Age > 50
    """

    new_dataset = envi.gcloud.BQ.query(query).to_dataframe()

    assert len(new_dataset) > 0