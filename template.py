import os
from pathlib import Path


list_of_files = [
    "src/__init__.py",

    # Components Module
    "src/Components/__init__.py",
    "src/Components/Data_Ingestion.py",
    "src/Components/Data_Validation.py",
    "src/Components/Data_Transformation.py",
    "src/Components/Model_Trainer.py",
    "src/Components/Model_Evaluation.py",
    "src/Components/Model_Pusher.py",

    # Documentation Module
    "docs/__init__.py",

    # Configuration Module
    "src/Configuration/__init__.py",
    "src/Configuration/MongoDB_Integration.py",

    # Constants Module
    "src/Constants/__init__.py",

    # Entity Module
    "src/Entity/__init__.py",
    "src/Entity/Config_Entity.py",
    "src/Entity/Artifact_Entity.py",

    # Exception Module
    "src/Exception/__init__.py",

    # Logger Module
    "src/Logger/__init__.py",

    # Pipeline Module
    "src/Pipelines/__init__.py",
    "src/Pipelines/Training_Pipeline.py",
    "src/Pipelines/Prediction_Pipeline.py",

    # Utility Module
    "src/Utils/__init__.py",
    "src/Utils/Main_Utils.py",

    # Notebook Module
    "Notebook_Experiments/__init__.py",

    # Model Configurations Module
    "Config/Model.yaml",
    "Config/Schema.yaml",

    "app.py",
    "Dockerfile",
    ".gitignore",
    ".dockerignore",
    "requirements.txt",
    "README.md",
    "setup.py" 
]

for filepath in list_of_files:

    # Convert to Path object
    filepath = Path(filepath) 

    # Split the path into directory and filename
    filedir, filename = os.path.split(filepath)

    # Create the directory if it does not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # Create the file if it does not exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"{filepath} already exists")