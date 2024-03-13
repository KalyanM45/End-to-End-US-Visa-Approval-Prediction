import os
from datetime import date
CURRENT_YEAR = date.today().year

# MongoDB Constants
DATABASE_NAME = "US_VISA"
COLLECTION_NAME = "US_DATA"
MONGODB_URL_KEY = "MONGODB_URL"

# Pipeline Constants
ARTIFACT_DIR: str = "Artifacts"
PIPELINE_NAME: str = "US_VISA"

# Model Constants
MODEL_FILE_NAME = "Model.pkl"
PREPROCSSING_OBJECT_FILE_NAME = "Preprocessor.pkl"

# Feature Constants
TARGET_COLUMN = "case_status"

# Data Constants
FILE_NAME: str = "Raw_Data.csv"
TRAIN_FILE_NAME: str = "Train_Data.csv"
TEST_FILE_NAME: str = "Test_Data.csv"

# Data Ingestion Constants
DATA_INGESTION_COLLECTION_NAME: str = "VISA_DATA"
DATA_INGESTION_DIR_NAME: str = "Data_Ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "Feature_Store"
DATA_INGESTION_INGESTED_DIR: str = "Ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

# Data Validation Constants
DATA_VALIDATION_DIR_NAME: str = "Data_Validation"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "Drift_Report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "Report.yaml"

# Data Transformation Constants
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

# Model Trainer Constants
MODEL_TRAINER_DIR_NAME: str = "Model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "Trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "Model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.7
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("Config", "Model.yaml")

# Model Evaluation Constants
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
MODEL_BUCKET_NAME = "usvisa-model"
MODEL_PUSHER_S3_KEY = "model-registry"

# Model Registry Constants
SCHEMA_FILE_PATH = os.path.join("Config", "Schema.yaml")

# AWS Constants
AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "us-east-1"

# API Constants
APP_HOST = "0.0.0.0"
APP_PORT = 8080