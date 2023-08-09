# Easy environment : easy-to-use Python environment management toolkit

**Easy Environment** is a Python tool that provides **easy-to-use functionality for managing files and data in different environments.** It offers a class that simplifies file operations on the local disk and cloud services such as Google Cloud (Google Cloud Storage and Big Query) or SharePoint.

## Features

* **File Formats**: Load and save files in various formats (PNG, JPG, XLSX, Parquet, CSV, Pickle) or [any other format](https://antoinepinto.gitbook.io/easy-environment/extra/customise-supported-formats).
* **Local Disk**: Support for local disk file handling (loading, saving, and management).
* **Google Cloud Storage**: Integration for loading and saving files.
* **Big Query Integration**: Append, write, and run queries on Big Query tables.
* **SharePoint Integration**: Download, upload, and manage files on SharePoint.

<p align="center">
  <img src="img/table_support.png" alt="drawing" width="500"/>
</p>

## Initialisation

To use Easy Environment, follow these instructions:

1. Install `easyenvi`

```python
pip install easyenvi
```

2. Create an instance of the `EasyEnvironment` class

All the parameters in the `EasyEnvironment` class are optional: it depends on how you use the tool. 

```python
from easyenvi import EasyEnvironment

env = EasyEnvironment(
  local_path='path/to/project/root', # Optional

  GCP_project_id='your-project-id', # Optional
  GCP_credential_path="path/to/credentials.json", # Optional
  GCS_path='gs://your-bucket-name/', # Optional

  sharepoint_site_url="https://{tenant}.sharepoint.com/sites/{site}", # Optional
  sharepoint_client_id="your-client-id", # Optional
  sharepoint_client_secret="your-client-secret", # Optional
                  )
```

Specifying certain parameters means certain dependencies: 
* For using Google Cloud, it is necessary to specify the project ID, the path to a credential .json file, and, in case of interaction with Google Cloud Storage, the path to the GCS folder (see [Google Cloud Initialisation](https://antoinepinto.gitbook.io/easy-environment/google-cloud-environment/google-cloud-initialisation)). Additionnaly, the installation of the libraries `google-cloud-storage` and `google-cloud-bigquery` is required. 
* For using SharePoint, it is necessary to specify the SharePoint site to interact with, as well as authentication credentials: either the client_id/client_secret pair or the username/user_password pair (see [SharePoint Initialisation](https://antoinepinto.gitbook.io/easy-environment/sharepoint-environment/sharepoint-initialisation)). Furthermore, the installation of the `Office365-REST-Python-Client` library is required.

## Examples of use

### Local features

```python
# Load any file format
my_dict = env.local.load(path='inputs/my_dictionnary.pickle')
my_logo = env.local.load(path='inputs/my_logo.png')
dataset = env.local.load(path='inputs/dataset.csv')

# Save any file format
env.local.save(obj=my_dict, path='outputs/my_dictionnary.pickle')
env.local.save(obj=my_logo, path='outputs/my_logo.png')
env.local.save(obj=dataset, path='outputs/dataset.csv')
```

### Google Cloud Storage features

```python
# Load any file format
my_dict = env.gcloud.GCS.load(path='inputs/my_dictionnary.pickle')
my_logo = env.gcloud.GCS.load(path='inputs/my_logo.png')
dataset = env.gcloud.GCS.load(path='inputs/dataset.csv')

# Save any file format
env.gcloud.GCS.save(obj=my_dict, path='outputs/my_dictionnary.pickle')
env.gcloud.GCS.save(obj=my_logo, path='outputs/my_logo.png')
env.gcloud.GCS.save(obj=dataset, path='outputs/dataset.csv')
```

### Big Query features

```python
df = pd.DataFrame(data={'age': [21, 52, 30], 'wage': [12, 17, 11]})

# Create a new table
env.gcloud.BQ.write(dataset, 'mydata.mytable')

# Append an existing table
env.gcloud.BQ.append(dataset, 'mydata.mytable')

# Run queries
query = """
SELECT *
FROM mydata.mytable
WHERE age < 40
"""

new_dataset = env.gcloud.BQ.query(query).to_dataframe()
```

### SharePoint features

```python
# Download a file
env.sharepoint.download(input_path="/sharepoint_folder/my_file.txt",
                        output_path="local_folder/my_file.txt")
                        
# Upload a file
env.sharepoint.upload(input_path="local_folder/my_file.txt",
                      output_path="sharepoint_folder/my_file.txt")
                      
# List files
env.sharepoint.list_files(folder="local_folder")
```

## Documentation

The documentation is available here : [Easy Environment - Documentation](https://antoinepinto.gitbook.io/easy-environment/)

## Future Improvements

Future releases of Easy Environment will include support for additional cloud storage providers, including Amazon Web Services (AWS) and Microsoft Azure.