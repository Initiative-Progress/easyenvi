class EasyEnvironment:
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

        if local_path is not None:

            from .disk import Disk
        
            self.local = Disk(root_path=local_path, loader_config=loader_config, saver_config=saver_config)

        if GCP_project_id is not None:

            from .gcp import GCP

            self.GCP = GCP(project_id=GCP_project_id, GCS_path=GCS_path, credential_path=GCP_credential_path,
                           loader_config=loader_config, saver_config=saver_config)