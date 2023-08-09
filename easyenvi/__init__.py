class EasyEnvironment:
    """
    Easy-to-use functionality for managing files and data in different environments (local, google cloud, sharepoint).
    
    Parameters:
    ----------
    local_path : str (optional)
        The path from which interactions with the local environment will be performed.
    gcloud_project_id : str (optional)
        The ID of the Google Cloud project.
    gcloud_credential_path : str (optional)
        The path to the .json Google Cloud credentials file.
    GCS_path : str (optional)
        The path from which interactions with Google Cloud Storage environment will be performed.
    sharepoint_site_url : str (optional)
        SharePoint site.
    sharepoint_client_id : str (optional)
        Client ID.
    sharepoint_client_secret : str (optional)
        Client secret.
    sharepoint_username : str (optional)
        User name of a SharePoint user account.
    sharepoint_user_password : str (optional)
        User password of a SharePoint user account.
    loader_config : dict (optional)
        Configuration for file loaders.
    saver_config : dict (optional)
        Configuration for file savers.

    Notes
    -----
    Multi-extension management: 
        By default, the extensions supported are .png, .jpg, .xlsx, .parquet, .csv, .parquet, .pickle. To integrate other extensions into the tool, see documentation "Customizing loader and saver".
    SharePoint environment:
        Need to obtain credentials: https://learn.microsoft.com/en-us/sharepoint/dev/solution-guidance/security-apponly-azureacs
        Either the pair client_id - client_secret is required, either the pair username - user_password
    """

    def __init__(self, local_path=None, gcloud_project_id=None, gcloud_credential_path=None,
                 GCS_path=None, sharepoint_site_url=None, sharepoint_client_id=None,
                 sharepoint_client_secret=None, sharepoint_username=None, 
                 sharepoint_user_password=None, loader_config=None, saver_config=None):

        if local_path is not None:

            from .disk import Disk
        
            self.local = Disk(
                root_path=local_path, 
                loader_config=loader_config, 
                saver_config=saver_config)

        if gcloud_project_id is not None:

            from .gcloud import gcloud

            self.gcloud = gcloud(
                project_id=gcloud_project_id, 
                GCS_path=GCS_path, 
                credential_path=gcloud_credential_path,
                loader_config=loader_config, 
                saver_config=saver_config)
            
        if sharepoint_site_url is not None:

            from .sharepoint import sharepoint

            self.sharepoint = sharepoint(
                site_url=sharepoint_site_url,
                client_id=sharepoint_client_id,
                client_secret=sharepoint_client_secret,
                username=sharepoint_username, 
                user_password=sharepoint_user_password
                        )