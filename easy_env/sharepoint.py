import os

from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential
from office365.runtime.auth.user_credential import UserCredential

class sharepoint:

    def __init__(self, site_url, client_id=None, client_secret=None, username=None, user_password=None):

        if client_id is not None:
            credentials = ClientCredential(client_id, client_secret)
        elif username is not None:
            credentials = UserCredential(username, user_password)

        self.env = ClientContext(site_url).with_credentials(credentials)

    def download(self, input_path, output_path):

        with open(output_path, "wb") as local_file:
           (self.env
            .web
            .get_file_by_server_relative_path(input_path)
            .download(local_file)
            .execute_query()
                     )
           
    def upload(self, input_path, output_path):
        
        with open(input_path, 'rb') as content_file:
            file_content = content_file.read()

        dir, name = os.path.split(output_path)
        self.env.web.get_folder_by_server_relative_url(dir).upload_file(name, file_content).execute_query()
           
    def list_files(self, folder):

        root_folder = self.env.web.get_folder_by_server_relative_path(folder)
        root_folder.expand(["Files", "Folders"]).get().execute_query()
        files = [file.properties['ServerRelativeUrl'].split('/')[-1] for file in root_folder.files]

        return files
    
    def delete_file(self, file_path):

        path_env = self.env.web.get_file_by_server_relative_url(file_path)
        path_env.delete_object().execute_query()