import pytest
import os
import sys

# ----------------------------------------------------------------------------- #
# Configuration de base pour les chemins d'accès au système
@pytest.fixture(autouse=True, scope='session')
def set_up_paths():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.append(base_dir)

# ----------------------------------------------------------------------------- #
@pytest.fixture(scope='session')
def load_environment():
    from dotenv import load_dotenv
    load_dotenv()

# ----------------------------------------------------------------------------- #
@pytest.fixture(scope='session')
def envi(load_environment):
    from easyenvi import EasyEnvironment

    envi = EasyEnvironment(
        local_path="",

        gcloud_project_id=os.getenv("GCLOUD_PROJECT_ID"),
        gcloud_credential_path="tests/credentials/my_credentials.json",
        GCS_path=os.getenv("GCS_path"),
        
        sharepoint_client_id=os.getenv("SHAREPOINT_CLIENT_ID"),
        sharepoint_client_secret=os.getenv("SHAREPOINT_CLIENT_SECRET"),
        sharepoint_site_url=os.getenv("SHAREPOINT_SITE_URL")
        )
    
    return envi