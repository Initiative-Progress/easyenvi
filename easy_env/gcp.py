import os

from google.cloud import storage, bigquery

from .file_manager import FileManager

class GCP:
    """
    A class representing the Google Cloud Platform.

    Args:
        GCP_project_id (str): The ID of the Google Cloud project.
        GCP_credential_path (str): The path to the Google Cloud credentials file.
        GCS_path (str): The base path of the Google Cloud Storage.
        loader_config (dict): Configuration for file loaders.
        saver_config (dict): Configuration for file savers.
    """

    def __init__(self, project_id, credential_path=None, GCS_path=None,
                 loader_config=None, saver_config=None):

        self.GCS = GCS(project_id=project_id, GCS_path=GCS_path, credential_path=credential_path,
                       loader_config=loader_config, saver_config=saver_config)
        self.BQ = BQ(project_id=project_id, credential_path=credential_path)

class BQ:
    """
    A class that handles data loading, writing, appending, and querying in BigQuery.

    Args:
        project_id (str): The ID of the Google Cloud project.
        credential_path (str): The path to the Google Cloud credentials file. Default is None.
    """

    def __init__(self, project_id, credential_path=None):

        self.project_id = project_id

        if credential_path is not None:
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path

    def load(self, path):
        """Loads data from the specified table path in BigQuery."""

        query = f"SELECT * FROM `{path}`"
        client = bigquery.Client(project=self.project_id)
        return client.query(query).result().to_dataframe()

    def write(self, obj, path, schema=None):
        """Writes data to the specified table path in BigQuery."""

        job_config = bigquery.LoadJobConfig(
            autodetect=True,
            source_format=bigquery.SourceFormat.PARQUET,
            write_disposition='WRITE_TRUNCATE'
        )

        # Create schema if not specified
        if schema is None:
            replacing = {'O': 'STRING', 'float64': 'FLOAT', 'float32': 'FLOAT', '<M8[ns]': 'TIMESTAMP', 'int64': 'INT64', 'bool': 'BOOL'}
            schema = obj.dtypes.replace(replacing).reset_index().values.tolist()

        job_config.schema = [bigquery.SchemaField(name, type_) for name, type_ in schema]

        client = bigquery.Client(project=self.project_id)
        client.load_table_from_dataframe(obj, path, job_config=job_config)

        return {'schema': schema}

    def append(self, obj, path):
        """Appends data to the specified BigQuery table."""

        job_config = bigquery.LoadJobConfig(
            autodetect=True,
            source_format=bigquery.SourceFormat.PARQUET,
            write_disposition='WRITE_APPEND'
        )

        client = bigquery.Client(project=self.project_id)
        client.load_table_from_dataframe(obj, path, job_config=job_config)
 
    def query(self, query):
        """Executes a query in BigQuery and returns the result."""

        client = bigquery.Client(project=self.project_id)
        return client.query(query)

class GCS:
    """
    A class that handles file operations on Google Cloud Storage (GCS).

    Args:
        project_id (str): The ID of the Google Cloud project.
        credential_path (str): The path to the Google Cloud credentials file. Default is None.
        GCS_path (str): The base path on GCS. Default is None.
        loader_config (dict): Configuration for file loaders.
        saver_config (dict): Configuration for file savers.
    """

    def __init__(self, project_id, credential_path=None, GCS_path=None, loader_config=None, saver_config=None):
    
        self.project_id = project_id
        self.GCS_path = GCS_path
        self.file_manage = FileManager(loader_config, saver_config)

        if credential_path is not None:
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path

    def get_blob(self, path):
        """Retrieves a blob (file) from the specified path in Google Cloud Storage."""

        full_path = self.GCS_path + path
        bucket_name, path = full_path[5:].split('/', 1)
        blob = storage.Client(project=self.project_id).bucket(bucket_name).blob(path)
        return blob

    def load(self, path):
        """Loads a file from the specified path on Google Cloud Storage."""

        extension = path.split('.')[-1]
        blob = self.get_blob(path)
        with blob.open('rb') as file:
            return self.file_manage.load(file, extension)

    def save(self, obj, path):
        """Saves an object to the specified path on Google Cloud Storage."""

        extension = path.split('.')[-1]

        if extension in ['png', 'jpg']:
            raise Exception("Saving extension unsupported by the saver")

        blob = self.get_blob(path)
        with blob.open('wb', ignore_flush=True) as f:
            self.file_manage.save(obj, f, extension)