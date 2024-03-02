import os
from datetime import date
CURRENT_YEAR = date.today().year

# MongoDB Constants
DATABASE_NAME = "US_VISA"
COLLECTION_NAME = "US_DATA"
MONGODB_URL_KEY = "MONGODB_URL"

# Model Constants
ARTIFACT_DIR: str = "Artifacts"
MODEL_FILE_NAME = "Model.pkl"
PREPROCSSING_OBJECT_FILE_NAME = "Preprocessor.pkl"

# Feature Constants
TARGET_COLUMN = "case_status"

# Data Constants
FILE_NAME: str = "Raw_Data.csv"
TRAIN_FILE_NAME: str = "Train_Data.csv"
TEST_FILE_NAME: str = "Test_Data.csv"