import os

from .file_manager import FileManager

class Disk:
    """
    Allows interaction with local environment.

    Parameters
    ----------
    local_path : str
        The path from which interactions with the local environment will be performed.
    loader_config : dict
        Configuration for file loaders. Default is None.
    saver_config :dict
        Configuration for file savers. Default is None.
    """

    def __init__(self, root_path, loader_config=None, saver_config=None):
        self.root_path = root_path
        self.file_manage = FileManager(loader_config, saver_config)

    def load(self, path):
        """
        Load a file.
        By default, the extensions supported are .png, .jpg, .xlsx, .parquet, .csv, .parquet, .pickle. To integrate other extensions into the tool, see documentation "Customizing loader and saver".
        
        Parameters
        ----------
        path : str
            path to load from.
        """

        load_path = os.path.join(self.root_path, path)
        extension = path.split('.')[-1]
        return self.file_manage.load(load_path, extension)

    def save(self, obj, path):
        """
        Save a file
        By default, the extensions supported are .png, .jpg, .xlsx, .parquet, .csv, .parquet, .pickle. To integrate other extensions into the tool, see documentation "Customizing loader and saver".
        
        Parameters
        ----------
        obj
            object to save.
        path : str
            path to save to.
        """

        save_path = os.path.join(self.root_path, path)
        extension = path.split('.')[-1]
        self.file_manage.save(obj, save_path, extension)

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