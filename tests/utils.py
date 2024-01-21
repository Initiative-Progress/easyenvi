from easyenvi import EasyEnvironment, file

def load_envi():

    secrets = file.load('credentials/secrets.toml')

    envi = EasyEnvironment(
        local_path='',

        gcloud_project_id=secrets['gcloud_project_id'],
        gcloud_credential_path="credentials/my_credentials.json",
        GCS_path=secrets['GCS_path'],
        
        sharepoint_client_id=secrets['sharepoint_client_id'],
        sharepoint_client_secret=secrets['sharepoint_client_secret'],
        sharepoint_site_url=secrets['sharepoint_site_url']
        )
    
    return envi