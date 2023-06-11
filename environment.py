import pickle
import os
import pandas as pd
from PIL import Image
from google.cloud import bigquery, storage

class Environment:
    """
    A class representing an environment.
    
    Args:
        local_path (str): The root path for local storage.
        GCP_project_id (str): The ID of the Google Cloud project.
        GCP_credential_path (str): The path to the Google Cloud credentials file.
        GCS_path (str): The base path of the Google Cloud Storage.
        loader_config (dict): Configuration for file loaders.
        saver_config (dict): Configuration for file savers.
    """

    def __init__(self, local_path=None, GCP_project_id=None, GCP_credential_path=None,
                  GCS_path=None, loader_config=None, saver_config=None):

        self.GCP = GCP(project_id=GCP_project_id, GCS_path=GCS_path, credential_path=GCP_credential_path,
                        loader_config=loader_config, saver_config=saver_config)
        
        self.local = Disk(root_path=local_path, loader_config=loader_config, saver_config=saver_config)

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
            replacing = {'O': 'STRING', 'float64': 'FLOAT', '<M8[ns]': 'TIMESTAMP', 'int64': 'INT64', 'bool': 'BOOL'}
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

class Disk:
    """
    A class that represents a local disk for file operations.

    Args:
        root_path (str): The root path of the disk.
        loader_config (dict): Configuration for file loaders. Default is None.
        saver_config (dict): Configuration for file savers. Default is None.
    """

    def __init__(self, root_path, loader_config=None, saver_config=None):
        self.root_path = root_path
        self.file_manage = FileManager(loader_config, saver_config)

    def load(self, path):
        """Loads a file from the specified path on the disk."""

        load_path = os.path.join(self.root_path, path)
        extension = path.split('.')[-1]
        return self.file_manage.load(load_path, extension)

    def save(self, obj, path):
        """Saves an object to the specified path on the disk."""

        save_path = os.path.join(self.root_path, path)
        extension = path.split('.')[-1]
        self.file_manage.save(obj, save_path, extension)

    def clear_folder(self, path):
        """Clears all files in the specified folder path."""
        folder_path = os.path.join(self.root_path, path)
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)

class FileManager:
    """
    A class that manages loading and saving files using various formats.
    
    Args:
        loader_config (dict): Configuration for file loaders.
        saver_config (dict): Configuration for file savers.
    """

    def __init__(self, loader_config=None, saver_config=None):
        
        if loader_config is None:
            self.loader_config = {
                'png':      Image.open,
                'jpg':      Image.open,
                'xlsx':     pd.read_excel,
                'parquet':  pd.read_parquet,
                'csv':      pd.read_csv,
                'pickle':   pickle.load
            }

        if saver_config is None:
            self.saver_config = {
                'png':      {'func': 'save',        'args': {}},
                'jpg':      {'func': 'save',        'args': {}},
                'xlsx':     {'func': 'to_excel',    'args': {}},
                'parquet':  {'func': 'to_parquet',  'args': {'index': False}},
                'csv':      {'func': 'to_csv',      'args': {'index': False}}
            }

    def load(self, path, extension):
        """Loads a file from the specified path and extension."""
        
        loader = self.loader_config[extension]
        if (extension == 'pickle') & (isinstance(path, str)):
            with open(path, 'rb') as file:
                return loader(file)
        else:
            return loader(path)
        
    def save(self, obj, path, extension):
        """Saves an object to the specified path with the given extension."""

        if extension == 'pickle':
            if isinstance(path, str):
                with open(path, 'wb') as file:
                    pickle.dump(obj, file, protocol=pickle.HIGHEST_PROTOCOL)
            else:
                pickle.dump(obj, path, protocol=pickle.HIGHEST_PROTOCOL)
        else:
            if extension not in self.saver_config.keys():
                raise Exception("Saving extension unsupported by the saver")

            func, args = self.saver_config[extension].values()
            
            saver = getattr(obj, func)
            saver(path, **args)