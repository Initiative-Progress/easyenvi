class FileManager:
    """
    Manages loading and saving files using various formats.
    
    Parameters
    ----------
    extra_loader_config : dict
        Extra configuration for file loaders.
    extra_saver_config : dict
        Extra configuration for file savers.
    """

    def __init__(self, extra_loader_config=None, extra_saver_config=None):

        self.loader_config = {
            'csv':      (csv_loader,        'rb'),
            'docx':     (docx_loader,       'rb'),
            'jpg':      (jpg_loader,        'rb'),
            'json':     (json_loader,       'rt'),
            'md':       (md_loader,         'rt'),
            'parquet':  (parquet_loader,    'rb'),
            'pdf':      (pdf_loader,        'rb'),
            'pickle':   (pickle_loader,     'rb'),
            'png':      (png_loader,        'rb'),
            'pptx':     (pptx_loader,       'rb'),
            'sql':      (sql_loader,        'rt'),
            'toml':     (toml_loader,       'rt'),
            'txt':      (txt_loader,        'rt'),
            'xlsx':     (xlsx_loader,       'rb'),
            'xml':      (xml_loader,        'rb'),
            'yaml':     (yaml_loader,       'rt'),
            'yml':      (yaml_loader,       'rt')
        }
        
        self.saver_config = {
            'csv':      (csv_saver,         'wb'),
            'docx':     (docx_saver,        'wb'),
            'jpg':      (jpg_saver,         'wb'),
            'json':     (json_saver,        'wt'),
            'md':       (md_saver,          'wt'),
            'parquet':  (parquet_saver,     'wb'),
            'pdf':      (pdf_saver,         'wb'),
            'pickle':   (pickle_saver,      'wb'),
            'png':      (png_saver,         'wb'),
            'pptx':     (pptx_saver,        'wb'),
            'sql':      (sql_saver,         'wt'),
            'toml':     (toml_saver,        'wt'),
            'txt':      (txt_saver,         'wt'),
            'xlsx':     (xlsx_saver,        'wb'),
            'xml':      (xml_saver,         'wb'),
            'yaml':     (yaml_saver,        'wt'),
            'yml':      (yaml_saver,        'wt')
        }

        if extra_loader_config is not None:
            self.loader_config.update(extra_loader_config)

        if extra_saver_config is not None:
            self.saver_config.update(extra_saver_config)

# CSV
def csv_loader(path, **kwargs):
    import pandas as pd
    return pd.read_csv(path, **kwargs)

def csv_saver(obj, path, **kwargs):
    obj.to_csv(path, **kwargs)

# DOCX
def docx_loader(path):
    from docx import Document
    return Document(path)

def docx_saver(obj, path):
    obj.save(path)

# JPG
def jpg_loader(path, **kwargs):
    from PIL import Image
    return Image.open(path, **kwargs).copy()

def jpg_saver(obj, path, **kwargs):
    obj.save(path, **kwargs)

# JSON
def json_loader(path, **kwargs):
    import json
    return json.load(path, **kwargs)

def json_saver(obj, path, **kwargs):
    import json
    json.dump(obj, path, **kwargs)

# MD
def md_loader(path, **kwargs):
    return path.read(**kwargs)

def md_saver(obj, path, **kwargs):
    path.write(obj, **kwargs)

# PARQUET
def parquet_loader(path, **kwargs):
    import pandas as pd
    return pd.read_parquet(path, **kwargs)

def parquet_saver(obj, path, **kwargs):
    obj.to_parquet(path, **kwargs)

# PDF
def pdf_loader(path):
    from PyPDF2 import PdfReader
    # return PdfReader(path)
    import copy
    return copy.deepcopy(PdfReader(path))

def pdf_saver(obj, path):
    from PyPDF2 import PdfWriter
    output = PdfWriter()
    for page in obj.pages:
        output.add_page(page)
    
    output.write(path)

# PICKLE
def pickle_loader(path, **kwargs):
    import pickle
    return pickle.load(path, **kwargs)

def pickle_saver(obj, path, **kwargs):
    import pickle
    pickle.dump(obj, path, protocol=pickle.HIGHEST_PROTOCOL, **kwargs)

# PPTX
def pptx_loader(path):
    from pptx import Presentation
    return Presentation(path)

def pptx_saver(obj, path):
    obj.save(path)

# PNG
def png_loader(path, **kwargs):
    from PIL import Image
    return Image.open(path, **kwargs).copy()

def png_saver(obj, path, **kwargs):
    obj.save(path, **kwargs)

# SQL
def sql_loader(path, **kwargs):
    return path.read(**kwargs)

def sql_saver(obj, path, **kwargs):
    path.write(obj, **kwargs)

# TOML
def toml_loader(path, **kwargs):
    import toml
    return toml.load(path, **kwargs)

def toml_saver(obj, path, **kwargs):
    import toml
    toml.dump(obj, path, **kwargs)

# TXT
def txt_loader(path, **kwargs):
    return path.read(**kwargs)

def txt_saver(obj, path, **kwargs):
    path.write(obj, **kwargs)

# XML
def xml_loader(path, **kwargs):
    import xml.etree.ElementTree as ET
    tree = ET.parse(path, **kwargs)
    root = tree.getroot()
    return root

def xml_saver(obj, path, **kwargs):
    import xml.etree.ElementTree as ET
    tree = ET.ElementTree(obj)
    tree.write(path, **kwargs)

# XLSX
def xlsx_loader(path, **kwargs):
    import pandas as pd
    return pd.read_excel(path, **kwargs)

def xlsx_saver(obj, path, **kwargs):
    obj.to_excel(path, **kwargs)

# YAML
def yaml_loader(path, **kwargs):
    import yaml
    return yaml.safe_load(path, **kwargs)

def yaml_saver(obj, path, **kwargs):
    import yaml
    yaml.dump(obj, path, **kwargs)