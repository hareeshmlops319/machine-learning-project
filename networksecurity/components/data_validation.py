from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.logging.logger import logging
from networksecurity.utils.main_utils.utils import read_yaml_file, write_yaml_file
from scipy.stats import ks_2samp
import pandas as pd
import numpy as np
import sys,os

class DataValidation:
    def __init__(self,data_validation_config: DataValidationConfig,data_ingestion_artifact: DataIngestionArtifact):
        try:
            self.data_validation_config=data_validation_config
            self.data_ingestion_artifact=data_ingestion_artifact
            self._schmema_config=read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e,self)
    @staticmethod
    def read_data(file_path:str)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def validate_number_of_columns(self,dataframe:pd.DataFrame)->bool:
        try:
            number_of_columns=len(self._schmema_config)
            logging.info(f"Required number of columns: {number_of_columns}")
            logging.info(f"Dataframe has columns: {len(dataframe.columns)}")
            if len(dataframe.columns)==number_of_columns:
                return True
            return False
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def detect_data_drift(self,base_df:pd.DataFrame,current_df:pd.DataFrame,threshold=0.05)->bool:
        try:
            status=True
            report={}
            for column in base_df.columns:
                d1=base_df[column]
                d2=current_df[column]
                is_sample_dist=ks_2samp(d1,d2)
                if threshold<=is_sample_dist.pvalue:
                    is_found=False
                else:
                    is_found=True
                    status=False
                
                report.update({column:{
                        "p_value":float(is_sample_dist.pvalue),
                        "drift_status":is_found
                    }})
            drift_report_file_path = self.data_validation_config.drift_report_file_path
        except Exception as e:
            raise NetworkSecurityException(e,self)        


     # validate  number of columns
    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            training_file_path=self.data_ingestion_artifact.trained_file_path
            testing_file_path=self.data_ingestion_artifact.test_file_path

            train_dataframe=DataValidation.read_data(training_file_path)
            test_dataframe=DataValidation.read_data(testing_file_path)

            # validate number of columns
            status=self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                error_message=f"Dataframe does not contain all the required columns.\n"

            status=self.validate_number_of_columns(dataframe=test_dataframe)
            if not status:
                error_message=f"Dataframe does not contain all the required columns.\n"
            
        except Exception as e:
            raise NetworkSecurityException(e,self)        
