import pickle

class FileManager:
    """
    A class that manages loading and saving files using various formats.
    
    Args:
        loader_config (dict): Configuration for file loaders.
        saver_config (dict): Configuration for file savers.
    """

    def __init__(self, loader_config=None, saver_config=None):
        
        if loader_config is None:

            from PIL import Image

            import pandas as pd

            self.loader_config = {
                'png':      Image.open,
                'jpg':      Image.open,
                'xlsx':     pd.read_excel,
                'parquet':  pd.read_parquet,
                'csv':      pd.read_csv,
                'pickle':   pickle.load
            }

        else:

            self.loader_config = loader_config

        if saver_config is None:
            self.saver_config = {
                'png':      {'func': 'save',        'args': {}},
                'jpg':      {'func': 'save',        'args': {}},
                'xlsx':     {'func': 'to_excel',    'args': {}},
                'parquet':  {'func': 'to_parquet',  'args': {'index': False}},
                'csv':      {'func': 'to_csv',      'args': {'index': False}}
            }
        
        else:
            
            self.saver_config = saver_config

    def load(self, path, extension):
        """Loads a file from the specified path and extension."""
        
        loader = self.loader_config[extension]
        if (extension == 'pickle') & (isinstance(path, str)):
            with open(path, 'rb') as file:
                return loader(file)
        else:
            return loader(path)
        
    def save(self, obj, path, extension):
        """Saves an object to the specified path with the given extension."""

        if extension == 'pickle':
            if isinstance(path, str):
                with open(path, 'wb') as file:
                    pickle.dump(obj, file, protocol=pickle.HIGHEST_PROTOCOL)
            else:
                pickle.dump(obj, path, protocol=pickle.HIGHEST_PROTOCOL)
        else:
            if extension not in self.saver_config.keys():
                raise Exception("Saving extension unsupported by the saver")

            func, args = self.saver_config[extension].values()
            
            saver = getattr(obj, func)
            saver(path, **args)