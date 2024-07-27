import fsspec

# CSV
def csv_loader(path, **kwargs):
    import pandas as pd
    
    with fsspec.open(path, 'rb', **kwargs) as f:
        return pd.read_csv(f)

def csv_saver(obj, path, **kwargs):
    with fsspec.open(path, 'wb', **kwargs) as f:
        obj.to_csv(f)

# DOCX
def docx_loader(path, **kwargs):
    from docx import Document
    
    with fsspec.open(path, 'rb', **kwargs) as f:
        return Document(f)

def docx_saver(obj, path, **kwargs):
    with fsspec.open(path, 'wb', **kwargs) as f:
        obj.save(f)

# JPG
def jpg_loader(path, **kwargs):
    from PIL import Image
    
    with fsspec.open(path, 'rb', **kwargs) as f:
        return Image.open(f).copy()

def jpg_saver(obj, path, **kwargs):
    with fsspec.open(path, 'wb', **kwargs) as f:
        obj.save(f)

# JSON
def json_loader(path, **kwargs):
    import json
    
    with fsspec.open(path, 'rt', **kwargs) as f:
        return json.load(f)

def json_saver(obj, path, **kwargs):
    import json
    
    with fsspec.open(path, 'wt', **kwargs) as f:
        json.dump(obj, f)

# MD
def md_loader(path, **kwargs):
    with fsspec.open(path, 'rt', **kwargs) as f:
        return f.read()

def md_saver(obj, path, **kwargs):
    with fsspec.open(path, 'wt', **kwargs) as f:
        f.write(obj)

# PARQUET
def parquet_loader(path, **kwargs):
    import pandas as pd
    
    with fsspec.open(path, 'rb', **kwargs) as f:
        return pd.read_parquet(f)

def parquet_saver(obj, path, **kwargs):
    with fsspec.open(path, 'wb', **kwargs) as f:
        obj.to_parquet(f)

# PDF
def pdf_loader(path, **kwargs):
    import copy
    from PyPDF2 import PdfReader
    
    with fsspec.open(path, 'rb', **kwargs) as f:
        return copy.deepcopy(PdfReader(f))

def pdf_saver(obj, path, **kwargs):
    from PyPDF2 import PdfWriter
    
    with fsspec.open(path, 'wb', **kwargs) as f:
        output = PdfWriter()
        for page in obj.pages:
            output.add_page(page)
    
        output.write(f)

# PICKLE
def pickle_loader(path, **kwargs):
    import pickle
    
    with fsspec.open(path, 'rb', **kwargs) as f:
        return pickle.load(f)

def pickle_saver(obj, path, **kwargs):
    import pickle
    
    with fsspec.open(path, 'wb', **kwargs) as f:
        pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)

# PPTX
def pptx_loader(path, **kwargs):
    from pptx import Presentation

    with fsspec.open(path, 'rb', **kwargs) as f:
        return Presentation(f)

def pptx_saver(obj, path, **kwargs):
    with fsspec.open(path, 'wb', **kwargs) as f:
        obj.save(f)

# PNG
def png_loader(path, **kwargs):
    from PIL import Image
    
    with fsspec.open(path, 'rb', **kwargs) as f:
        return Image.open(f).copy()

def png_saver(obj, path, **kwargs):
    with fsspec.open(path, 'wb', **kwargs) as f:
        obj.save(f)

# SQL
def sql_loader(path, **kwargs):
    with fsspec.open(path, 'rt', **kwargs) as f:
        return f.read()

def sql_saver(obj, path, **kwargs):
    with fsspec.open(path, 'wt', **kwargs) as f:
        f.write(obj)

# TOML
def toml_loader(path, **kwargs):
    import toml

    with fsspec.open(path, 'rt', **kwargs) as f:
        return toml.load(f)

def toml_saver(obj, path, **kwargs):
    import toml
    
    with fsspec.open(path, 'wt', **kwargs) as f:
        toml.dump(obj, f)

# TXT
def txt_loader(path, **kwargs):
    with fsspec.open(path, 'rt', **kwargs) as f:
        return f.read()

def txt_saver(obj, path, **kwargs):
    with fsspec.open(path, 'wt', **kwargs) as f:
        f.write(obj)

# XML
def xml_loader(path, **kwargs):
    import xml.etree.ElementTree as ET

    with fsspec.open(path, 'rb', **kwargs) as f:
        tree = ET.parse(f)
        root = tree.getroot()
        return root

def xml_saver(obj, path, **kwargs):
    import xml.etree.ElementTree as ET

    with fsspec.open(path, 'wb', **kwargs) as f:
        tree = ET.ElementTree(obj)
        tree.write(f)

# XLSX
def xlsx_loader(path, **kwargs):
    import pandas as pd
    
    with fsspec.open(path, 'rb', **kwargs) as f:
        return pd.read_excel(f)

def xlsx_saver(obj, path, **kwargs):
    with fsspec.open(path, 'wb', **kwargs) as f:
        obj.to_excel(f)

# YAML
def yaml_loader(path, **kwargs):
    import yaml
    
    with fsspec.open(path, 'rt', **kwargs) as f:
        return yaml.safe_load(f)

def yaml_saver(obj, path, **kwargs):
    import yaml
    
    with fsspec.open(path, 'wt', **kwargs) as f:
        yaml.dump(obj, f)