from easyenvi.file import format_converter

loader_config = {
    'csv':      format_converter.csv_loader,
    'docx':     format_converter.docx_loader,
    'jpg':      format_converter.jpg_loader,
    'json':     format_converter.json_loader,
    'md':       format_converter.md_loader,
    'parquet':  format_converter.parquet_loader,
    'pdf':      format_converter.pdf_loader,
    'pickle':   format_converter.pickle_loader,
    'png':      format_converter.png_loader,
    'pptx':     format_converter.pptx_loader,
    'sql':      format_converter.sql_loader,
    'toml':     format_converter.toml_loader,
    'txt':      format_converter.txt_loader,
    'xlsx':     format_converter.xlsx_loader,
    'xml':      format_converter.xml_loader,
    'yaml':     format_converter.yaml_loader,
    'yml':      format_converter.yaml_loader
}

saver_config = {
    'csv':      format_converter.csv_saver,
    'docx':     format_converter.docx_saver,
    'jpg':      format_converter.jpg_saver,
    'json':     format_converter.json_saver,
    'md':       format_converter.md_saver,
    'parquet':  format_converter.parquet_saver,
    'pdf':      format_converter.pdf_saver,
    'pickle':   format_converter.pickle_saver,
    'png':      format_converter.png_saver,
    'pptx':     format_converter.pptx_saver,
    'sql':      format_converter.sql_saver,
    'toml':     format_converter.toml_saver,
    'txt':      format_converter.txt_saver,
    'xlsx':     format_converter.xlsx_saver,
    'xml':      format_converter.xml_saver,
    'yaml':     format_converter.yaml_saver,
    'yml':      format_converter.yaml_saver
}

def load(path, **kwargs):

    extension = path.split('.')[-1]

    if extension not in loader_config:
        raise ValueError(f"Extension '{extension}' is not currently supported.")

    loader = loader_config[extension]

    return loader(path, **kwargs)

def save(obj, path, **kwargs):

    extension = path.split('.')[-1]

    if extension not in saver_config:
        raise ValueError(f"Extension '{extension}' is not currently supported.")

    saver = saver_config[extension]

    return saver(obj, path, **kwargs)