from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig



if __name__=='__main__':
    try:
        TrainingPipelineConfig=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(training_pipeline_config=TrainingPipelineConfig)
        data_ingestion=DataIngestion(data_ingestion_config=data_ingestion_config)
        logging.info("Starting data ingestion")
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        logging.info("Completed data ingestion")
        data_validation_config=DataValidationConfig(training_pipeline_config=TrainingPipelineConfig)
        data_validation=DataValidation(data_validation_config=data_validation_config,data_ingestion_artifact=data_ingestion_artifact)
        logging.info("Starting data validation")
        data_validation.initiate_data_validation()
        print(data_ingestion_artifact)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
        