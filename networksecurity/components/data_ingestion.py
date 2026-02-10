from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
import os
import numpy as np
import pandas as pd
import pymongo
from sklearn.model_selection import train_test_split
from networksecurity.entity.artifact_entity import DataIngestionArtifact


from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")


class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e,self)
        
    def export_collection_as_dataframe(self):
        """ Read the data from Mongo DB and export it as a pandas dataframe."""
        try:
            databse_name=self.data_ingestion_config.database_name
            collection_name=self.data_ingestion_config.collection_name
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            collection=self.mongo_client[databse_name][collection_name]
            df=pd.DataFrame(list(collection.find()))
            if "_id" in df.columns:
                df=df.drop("_id",axis=1)
                df.replace({"na":np.NAN},inplace=True)
                return df
        except Exception as e:
            raise NetworkSecurityException(e,self)
    
    def export_data_into_feature_store(self,df:pd.DataFrame):
        try:
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            dir_path=os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            df.to_csv(feature_store_file_path,index=False,header=True)
        except Exception as e:
            raise NetworkSecurityException(e,self)
    def split_data_as_train_test(self,df:pd.DataFrame):
        try:
            train_set, test_set = train_test_split(
                df, test_size=self.data(df, test_size=self.data_ingestion_config.train_test_split_ration)
            )
            logging.info("Performed train test split on the dataframe")
            logging.info("Excited split_data_as_train_test method of Data_Ingesation class")
            dir_path=os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info("Exporting training and testing data to respective file paths")
            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True
                             )
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)
            logging.info("Exported training and testing data to respective file paths")
    
        except Exception as e:
            raise NetworkSecurityException(e,self)
    

    
    def initiate_data_ingestion(self):
        try:
            dataframe=self.export_collection_as_dataframe()
            dataframe=self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)
            DataIngestionArtifact=self.DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
                                                             test_file_path=self.data_ingestion_config.testing_file_path)
            return DataIngestionArtifact

        except Exception as e:
            raise NetworkSecurityException(e,self)



    



    

