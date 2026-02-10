from networksecurity.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
import os
import numpy as np
import pandas as pd
import pymongo
from sklearn.model_selection import train_test_split


from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")


class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)


    



    

