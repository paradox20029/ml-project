import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException
from src.logger import logging

def start_training_pipeline():
    try:
        logging.info("Starting training pipeline")
        
        # Data Ingestion
        data_ingestion = DataIngestion()
        train_path, test_path = data_ingestion.initiate_data_ingestion()
        
        # Data Transformation
        data_transformation = DataTransformation()
        train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(train_path, test_path)
        
        # Model Training
        model_trainer = ModelTrainer()
        r2_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
        
        logging.info(f"Training pipeline completed with R2 score: {r2_score}")
        return r2_score
        
    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    start_training_pipeline()