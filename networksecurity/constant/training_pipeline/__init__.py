import os
import sys
import numpy as np
import pandas as pd

"""
defining common constant variable for a training pipeline
"""
TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "Networksecurity"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "phisingData.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"



"""
Data Ingestion releated constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str = "hareeshyalamasetty"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2


