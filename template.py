import os
from pathlib import Path
import logging

logging.basicConfig(level= logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "TextSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/pipeline/__init__.py"
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "app.py",
    "main.py",
    "setup.py",
    "requirements.py",
    "params.yaml",
    "config/config.yaml",
    "Dockerfile",
    "research/trials.ipynb"

]



for file in list_of_files:
    file_path = Path(file)
    filedir, filename = os.path.split(file_path)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory {filedir} for {filename}")
    else:
        logging.info(f"Directory {filedir} already exists")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)):
        with open(file_path, "w") as f:
            pass
        logging.info(f"Created file {file_path}")

    else:
        logging.info(f"File {file_path} already exists")





    
