import os
import sys
from pandas import DataFrame
from sklearn.model_selection import train_test_split

from src.Logger import logging
from src.Exception import CustomException
from src.Entity.Config_Entity import DataIngestionConfig
from src.Entity.Artifact_Entity import DataIngestionArtifact
from src.Utils.MongoDB_Data_Retrieve import USvisaData

'''
Data Ingestion Config contains paths used in this file:
1. Data_Ingestion Directory 
2. Feature store 
3. Training file
4. Testing file
5. Collection Name used to retrieve data from MongoDB
'''

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig=DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e,sys)

    def export_data_into_feature_store(self)->DataFrame:
        try:
            logging.info(f"Retreival Process from MongoDB Initiated from Collection: {self.data_ingestion_config.collection_name}")
            usvisa_data = USvisaData()
            dataframe = usvisa_data.export_collection_as_dataframe(collection_name = self.data_ingestion_config.collection_name)
            logging.info(f"Shape of DataFrame: {dataframe.shape}")

            feature_store_file_path  = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            logging.info(f"Exported Data into Feature Store: {feature_store_file_path}")

            return dataframe

        except Exception as e:
            raise CustomException(e,sys)

    def split_data_as_train_test(self,dataframe: DataFrame) ->None:

        logging.info("Initiating Data splitting for Training and Testing Process.")

        try:
            train_set, test_set = train_test_split(dataframe, test_size=0.2)
            logging.info("Done Splitting the dataframe into train and test set")

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)
            
            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)
            logging.info(f"Exported Training Data into: {self.data_ingestion_config.training_file_path}")
            logging.info(f"Exported Testing Data into: {self.data_ingestion_config.testing_file_path}")

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_ingestion(self) ->DataIngestionArtifact:

        logging.info("Initiating Data Ingestion Process")

        try:
            dataframe = self.export_data_into_feature_store()
            logging.info("Data Retreived from the MongoDB")

            self.split_data_as_train_test(dataframe)
            logging.info("Training and Testing Data split Done")

            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
            test_file_path=self.data_ingestion_config.testing_file_path)
            logging.info("Data Ingestion - Successfully Completed.")
            return data_ingestion_artifact
        except Exception as e:
            raise CustomException(e, sys) from e