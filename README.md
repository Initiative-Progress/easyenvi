# Easy environment : easy-to-use Python environment management toolkit

**Easy Environment** is a Python package that provides easy-to-use functionality for managing files and data in different environments. It offers a class called Environment that simplifies file operations on the local disk and cloud services such as Google Cloud (Google Cloud Storage and Big Query) or SharePoint.

## Features

* Load and save files in various formats such as PNG, JPG, XLSX, Parquet, CSV, and Pickle.
* Support for loading, saving and management file from local disk.
* Support for loading and saving files from Google Cloud Storage.
* Support append and write Big Query tables, as well as the ability to run queries.
* Supports the downloading, uploading and management of files on a SharePoint site.
* Flexible configuration for file loaders and savers.

<p align="center">
  <img src="img/table_support.png" alt="drawing" width="500"/>
</p>

## Initialize the Environment

To start using Easy Environment, create an instance of the `EasyEnvironment` class, providing the necessary parameters:

```python
from easy_env import EasyEnvironment

env = EasyEnvironment(
  local_path='path/to/project/root', # Optional

  GCP_project_id='your-project-id', # Optional
  GCP_credential_path="path/to/credentials.json", # Optional
  GCS_path='gs://your-bucket-name/' # Optional

  sharepoint_client_id="your-client-id", # Optional
  sharepoint_client_secret="your-client-secret", # Optional
  sharepoint_site_url="https://{tenant}.sharepoint.com/sites/{site}" # Optional
                  )
```

## Local File Operations

Easy Environment provides a `Disk` class for local file operations. You can access it through the `local` attribute of the `EasyEnvironment` instance.

```python
# Load/Save a pickle object
my_dictionnary = env.local.load('inputs/my_dictionnary.pickle')
env.local.save(my_dictionnary, 'outputs/my_dictionnary.pickle')

# Load/Save an image (png / jpg)
my_logo = env.local.load('inputs/my_logo.png')
env.local.save(my_logo, 'outputs/my_logo.png')

# Load/Save a dataset (csv / excel / jpg)
dataset = env.local.load('inputs/dataset.csv')
env.local.save(dataset, 'outputs/dataset.csv')
```

## Google Cloud Storage Operations

To perform file operations on Google Cloud Storage, use the `GCS` class accessible through the `GCP` attribute of the `EasyEnvironment` instance.

```python
# Load a pickle object
env.GCP.GCS.load(my_dictionnary, 'my_dictionnary.pickle')

# Save a parquet dataset
env.GCP.GCS.save(dataset, 'dataset.parquet')
```

## Big Query Operations

For working with BigQuery, use the `BQ` class accessible through the `GCP` attribute of the `EasyEnvironment` instance.

```python
# Create a table
env.GCP.BQ.write(dataset, 'mydata.mytable')

# Append a table
env.GCP.BQ.append(dataset, 'mydata.mytable')

# Make a query
query = """
SELECT 
  *
FROM 
  mydata.mytable
WHERE 
  Age > 50
"""

new_dataset = env.GCP.BQ.query(query).to_dataframe()
```

## Sharepoint

SharePoint operations are accessible via the `sharepoint` attribute of the `EasyEnvironment` instance.

```python
# Download a file
env.sharepoint.download(input_path="/folder/subfolder/my_file.csv",
                        output_path="my_file.csv")

# Upload a file
env.sharepoint.upload(input_path='my_file.csv',
                      output_path="/folder/subfolder/my_file.csv")

# List files in a folder
env.sharepoint.list_files(folder="folder/subfolder")

# Delete a file
env.sharepoint.delete_file(file_path="/folder/subfolder/my_file.csv")
```

## Customizing File Loaders and Savers

Easy Environment allows you to customize the file loaders and savers by providing configuration dictionaries during initialization. Here's an example:

```python
loader_config = {
    'txt':      txt_loader_function,
    'json':     json_loader_function,
    # Add more file extensions and corresponding loader functions
}

saver_config = {
    'txt':      {'func': 'txt_saver_function', 'args': {}},
    'json':     {'func': 'json_saver_function', 'args': {}},
    # Add more file extensions and corresponding saver functions and arguments
}

env = EasyEnvironment(
    local_path='path/to/project/root',
    GCP_project_id='your-project-id',
    GCP_credential_path="path/to/credentials.json",
    GCS_path='gs://your-bucket-name/',
    loader_config=loader_config,
    saver_config=saver_config
)
```

In the above example, you can specify custom loader and saver functions for file extensions not covered by the default configurations. Just replace 'txt_loader_function' and 'txt_saver_function' with your own loader and saver functions, respectively.

Make sure to import the necessary functions and libraries for your custom loaders and savers.

## Future Improvements

Future releases of Easy Environment will include support for additional cloud storage providers, including Amazon Web Services (AWS) and Microsoft Azure. This expansion aims to provide users with increased flexibility when working with cloud-based environments.