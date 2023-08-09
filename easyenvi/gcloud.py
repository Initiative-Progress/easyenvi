import os

from google.cloud import storage, bigquery

from .file_manager import FileManager

class gcloud:
    """
    Allows interaction with Google Cloud environment.

    Parameters
    ----------
    project_id : str
        The ID of the Google Cloud project.
    credential_path : str
        The path to the Google Cloud credentials file. Default is None.
    GCS_path : str
        The base path of the Google Cloud Storage.
    loader_config : dict
        Configuration for file loaders.
    saver_config : dict
        Configuration for file savers.
    """

    def __init__(self, project_id, credential_path=None, GCS_path=None,
                 loader_config=None, saver_config=None):

        self.GCS = GCS(project_id=project_id, GCS_path=GCS_path, credential_path=credential_path,
                       loader_config=loader_config, saver_config=saver_config)
        self.BQ = BQ(project_id=project_id, credential_path=credential_path)



class GCS:
    """
    Allows interaction with Google Cloud Storage environment.

    Parameters
    ----------
    project_id : str
        The ID of the Google Cloud project.
    credential_path : str
        The path to the Google Cloud credentials file. Default is None.
    GCS_path : str
        The base path on GCS. Default is None.
    loader_config : dict
        Configuration for file loaders.
    saver_config : dict
        Configuration for file savers.
    """

    def __init__(self, project_id, credential_path=None, GCS_path=None, loader_config=None, saver_config=None):
    
        self.project_id = project_id
        self.GCS_path = GCS_path
        self.file_manage = FileManager(loader_config, saver_config)

        if credential_path is not None:
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path

    def get_blob(self, path):
        """
        Retrieves a blob from the specified path in Google Cloud Storage.

        Parameters
        ----------
        path : str
            path to blob
        """

        full_path = self.GCS_path + path
        bucket_name, path = full_path[5:].split('/', 1)
        blob = storage.Client(project=self.project_id).bucket(bucket_name).blob(path)
        return blob

    def load(self, path):
        """
        Load a file from GCS
        By default, the extensions supported are .png, .jpg, .xlsx, .parquet, .csv, .parquet, .pickle. To integrate other extensions into the tool, see documentation "Customizing loader and saver".

        
        Parameters
        ----------
        path : str
            path to load from
        """

        extension = path.split('.')[-1]
        blob = self.get_blob(path)
        
        return self.file_manage.load(blob.open('rb'), extension)

    def save(self, obj, path):
        """
        Save a file to GCS
        By default, the extensions supported are .png, .jpg, .xlsx, .parquet, .csv, .parquet, .pickle. To integrate other extensions into the tool, see documentation "Customizing loader and saver".

        
        Parameters
        ----------
        obj
            object to save
        path : str
            path to save to
        """

        extension = path.split('.')[-1]

        if extension in ['png', 'jpg']:
            raise Exception("Saving extension unsupported by the saver")

        blob = self.get_blob(path)
        with blob.open('wb', ignore_flush=True) as f:
            self.file_manage.save(obj, f, extension)

    def list_files(self, path):
        """
        List files into a specific folder.
        
        Parameters
        ----------
        path : str
            path to list files
        """

        full_path = self.GCS_path + path
        bucket_name, path = full_path[5:].split('/', 1)
        client = storage.Client(project=self.project_id).bucket(bucket_name)
        files = [blob.name for blob in client.list_blobs(prefix=path)]

        return files
    
    def download(self, path, output_path):
        """
        Download a file from the specified path on Google Cloud Storage.
        
        Parameters
        ----------
        path : str
            path to the file to download
        output_path : str
            path to store the file
        """

        blob = self.get_blob(path)
        blob.download_to_filename(output_path)
    
class BQ:
    """
    Allows interaction with Google Cloud Big Query environment.

    Parameters:
    project_id : str
        The ID of the Google Cloud project.
    credential_path : str
        The path to the Google Cloud credentials file. Default is None.
    """

    def __init__(self, project_id, credential_path=None):

        self.project_id = project_id

        if credential_path is not None:
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path

    def load(self, path):
        """
        Load an entire Big Query table into Python.
        
        Parameters:
        path : str
            path representing the data set and the name of the table (ex : "mydata.mytable")
        """

        query = f"SELECT * FROM `{path}`"
        client = bigquery.Client(project=self.project_id)
        return client.query(query).result().to_dataframe()

    def write(self, obj, path, schema=None):
        """
        Write an entire Python dataframe into Big Query.
        
        Parameters
        ----------
        obj : pandas.DataFrame
            table to save
        path : str
            path representing the data set and the name of the table (ex : "mydata.mytable")
        schema : list (optional)
            schema of the table. If not specified, a schema is generated based on mapping
            Format: list of dictionnaries (see Documentation)
        """

        client = bigquery.Client(project=self.project_id)

        job_config = bigquery.LoadJobConfig(
            autodetect=True,
            source_format=bigquery.SourceFormat.PARQUET,
            write_disposition='WRITE_TRUNCATE'
        )

        if schema is not None:
            job_config.schema = schema

        client.load_table_from_dataframe(obj, path, job_config=job_config)

    def append(self, obj, path):
        """
        Append an existing Big Query table.
        
        Parameters
        ----------
        obj : pandas.DataFrame
            table to append
        path : str
            path representing the data set and the name of the table (ex : "mydata.mytable")
        """

        job_config = bigquery.LoadJobConfig(
            autodetect=True,
            source_format=bigquery.SourceFormat.PARQUET,
            write_disposition='WRITE_APPEND'
        )

        client = bigquery.Client(project=self.project_id)
        client.load_table_from_dataframe(obj, path, job_config=job_config)
 
    def query(self, query):
        """
        Execute Big Query query.
        
        Parameters
        ----------
        query : str
            query to execute
        """

        client = bigquery.Client(project=self.project_id)
        return client.query(query)