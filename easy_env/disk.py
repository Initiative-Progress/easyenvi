import os

from .file_manager import FileManager

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