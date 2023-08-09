import pickle

class FileManager:
    """
    Manages loading and saving files using various formats.
    
    Arguments:
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
                'pickle':   pickle_loader
            }

        else:

            self.loader_config = loader_config

        if saver_config is None:
            self.saver_config = {
                'png':      png_saver,
                'jpg':      jpg_saver,
                'xlsx':     xlsx_saver,
                'parquet':  parquet_saver,
                'csv':      csv_saver,
                'pickle':   pickle_saver
            }
        
        else:
            
            self.saver_config = saver_config

    def load(self, path, extension):
        """Loads a file from the specified path and extension."""
        
        if extension not in self.loader_config.keys():
            raise Exception("Saving extension unsupported by the saver")

        loader = self.loader_config[extension]
        return loader(path)
        
    def save(self, obj, path, extension):
        """Saves an object to the specified path with the given extension."""

        if extension not in self.saver_config.keys():
            raise Exception("Saving extension unsupported by the saver")

        saver = self.saver_config[extension]
        saver(obj, path)

def pickle_loader(path):
    if isinstance(path, str):
        with open(path, 'rb') as file:
            return pickle.load(file)
    else:
        pickle.load(path)
    
def pickle_saver(obj, path):
    if isinstance(path, str):
        with open(path, 'wb') as file:
            pickle.dump(obj, file, protocol=pickle.HIGHEST_PROTOCOL)
    else:
        pickle.dump(obj, path, protocol=pickle.HIGHEST_PROTOCOL)

def csv_saver(obj, path):
    obj.to_csv(path)

def parquet_saver(obj, path):
    obj.to_parquet(path)

def xlsx_saver(obj, path):
    obj.to_excel(path)

def png_saver(obj, path):
    obj.save(path)

def jpg_saver(obj, path):
    obj.save(path)