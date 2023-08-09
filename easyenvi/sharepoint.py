import os

from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential
from office365.runtime.auth.user_credential import UserCredential

class sharepoint:
    """
    Allows interaction with SharePoint environment.
    Need to obtain credentials: https://learn.microsoft.com/en-us/sharepoint/dev/solution-guidance/security-apponly-azureacs
    Either the pair client_id - client_secret is required, either the pair username - user_password

    Parameters
    ----------
    site_url : str
        SharePoint site.
    client_id : str (optional)
        Client id.
    client_secret : str (optional)
        Client secret.
    username : str (optional)
        User name of a SharePoint user account.
    user_password : str (optional)
        User password of a SharePoint user account.
    """

    def __init__(self, site_url, client_id=None, client_secret=None, username=None, user_password=None):

        if client_id is not None:
            credentials = ClientCredential(client_id, client_secret)
        elif username is not None:
            credentials = UserCredential(username, user_password)

        self.env = ClientContext(site_url).with_credentials(credentials)

    def download(self, input_path, output_path):
        """
        Download a file from SharePoint.
        
        Parameters
        ----------
        input_path : str
            Sharepoint path to the file to be downloaded
        output_path : str
            Local path to store the downloaded file
        """

        with open(output_path, "wb") as local_file:
           (self.env
            .web
            .get_file_by_server_relative_path(input_path)
            .download(local_file)
            .execute_query()
                     )
           
    def upload(self, input_path, output_path):
        """
        Upload a file into SharePoint.
        
        Parameters
        ----------
        input_path : str
            Local path to the file to be uploaded
        output_path : str
            SharePoint path to store the uploaded file
        """
        
        with open(input_path, 'rb') as content_file:
            file_content = content_file.read()

        dir, name = os.path.split(output_path)
        self.env.web.get_folder_by_server_relative_url(dir).upload_file(name, file_content).execute_query()
           
    def list_files(self, folder):
        """
        List the files in a SharePoint folder
        
        Parameters
        ----------
        folder : str
            Sharepoint access path for listing files
        """

        root_folder = self.env.web.get_folder_by_server_relative_path(folder)
        root_folder.expand(["Files", "Folders"]).get().execute_query()
        files = [file.properties['ServerRelativeUrl'].split('/')[-1] for file in root_folder.files]

        return files
    
    def delete_file(self, file_path):
        """
        Delete a file
        
        Parameters
        ----------
        file_path : str
            Sharepoint path of the file to be deleted
        """

        path_env = self.env.web.get_file_by_server_relative_url(file_path)
        path_env.delete_object().execute_query()