#This file contains project directory should be structured, It can be automate using cookiecutter

from pathlib import Path
import os  #it allows us to perform os related tasks & manupulation on file,directory,envirenment_variables more..
import logging  #It's helps us to see python programme runs smmothly,tracking down issue, helpful to maintain and debug the code

logging.basicConfig(level=logging.INFO)
project_name='ml'

list_of_files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/Pipeline/__init__.py",
    f"src/{project_name}/Pipeline/training.py",
    f"src/{project_name}/Pipeline/prediction.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/utiles.py",
    f"src/{project_name}/logger.py"

]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename =os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"current directory {filedir} of file name {filename}")

    if((not os.path.exists(filepath)) or (os.path.getsize(filepath)==0)):
        with open(filepath, "w") as f:
            pass
            logging.info(f"this is file name:{filepath}")
        
    else:
        logging.info(f"{filename} is already exist")

