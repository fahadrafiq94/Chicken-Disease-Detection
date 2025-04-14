import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# specify the project name
project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    # specify constructer to import the module
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "reserach/trials.ipynb"
]


for filepath in list_of_files:
    # use Path to handle file paths
    filepath = Path(filepath)
    # split the file path into directory and file name
    filedir, filename = os.path.split(filepath)

    # check if the file exists
    if filedir != "":
        # create the directory if it does not exist
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")
        
    # check if the file exists
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filename}")

    