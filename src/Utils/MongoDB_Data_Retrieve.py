import sys
import numpy as np
import pandas as pd
from typing import Optional

from src.Logger import logging
from src.Constants import DATABASE_NAME
from src.Exception import CustomException
from src.Configuration.MongoDB_Integration import MongoDBClient

# Class to retrieve the data from MongoDB
class USvisaData:
    # Connecting to MongoDB Clinet
    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise CustomException(e,sys)
        

    def export_collection_as_dataframe(self,collection_name:str,database_name:Optional[str]=None)->pd.DataFrame:
        # Exporting the collection as dataframe
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
                
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na":np.nan},inplace=True)
            logging.info("Exported Collection as a DataFrame from MongoDB.")
            return df
        
        except Exception as e:
            raise CustomException(e,sys)