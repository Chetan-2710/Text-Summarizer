# CMD: python template.py

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "TextSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep", # this is needed for CI/CD deployment, whenever we do the commit this will be taken by the could for deployment purpose
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py", # common will have utilities.
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]


for filepath in list_of_files:
    filepath = Path(filepath) # for handling the file path structure as i am using windows (which has backward slash) but gave forward slash.
    filedir, filename = os.path.split(filepath) # splits folder path and file path.

    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # This will create a folder if the folder is not present.
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}") 
    else:
        logging.info(f"{filename} is already exists")

# __init__.py is the constructor file, it is used for making a directory as a package and for controling what gets imported.