import os

from easyenvi import file

class disk:
    """
    Allows interaction with local environment.

    Parameters
    ----------
    local_path : str
        The path from which interactions with the local environment will be performed.
    extra_loader_config : dict
        Extra configuration for file loaders. Default is None.
    extra_saver_config :dict
        Extra configuration for file savers. Default is None.
    """

    def __init__(self, root_path, extra_loader_config=None, extra_saver_config=None):
        self.root_path = root_path
        
    def load(self, path, **kwargs):
        """
        Load a file.
        To learn more about the extensions supported by default, refer to the documentation : https://antoinepinto.gitbook.io/easy-environment/
        To integrate other extensions into the tool, see documentation "Customise supported formats": https://antoinepinto.gitbook.io/easy-environment/extra/customise-supported-formats

        Parameters
        ----------
        path : str
            path to load from.
        """

        load_path = os.path.join(self.root_path, path)
        return file.load(load_path)

    def save(self, obj, path, **kwargs):
        """
        Save a file
        To learn more about the extensions supported by default, refer to the documentation : https://antoinepinto.gitbook.io/easy-environment/
        To integrate other extensions into the tool, see documentation "Customise supported formats": https://antoinepinto.gitbook.io/easy-environment/extra/customise-supported-formats

        Parameters
        ----------
        obj
            object to save.
        path : str
            path to save to.
        """

        save_path = os.path.join(self.root_path, path)
        return file.save(obj, save_path)

    def clear_folder(self, path):
        """
        Clear a folder
        
        Parameters
        ----------
        path : str
            path at which to delete all files.
        """
        folder_path = os.path.join(self.root_path, path)
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)