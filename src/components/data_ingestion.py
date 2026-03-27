# # Data Ingestion Component
# #data ingestion is used to handle the ingestion of data from various sources, such as databases, APIs, or files. It is responsible for extracting data, transforming it into a suitable format, and loading it into a storage system or data warehouse for further processing and analysis.
# #read the data and split in train test 
# import os
# import sys
# import pandas as pd
# #using the logging and excpetion files 
# from src.exception import CustomException
# from src.logger import logging

# from sklearn.model_selection import train_test_split
# from dataclasses import dataclass   
# from src.components.data_transformation import DataTransformation
# from src.components.data_transformation import DataTransformationConfig

# '''the data ingestion class is used 
# to handle the data ingestion process, 
# which includes reading the data, splitting it into 
# training and testing sets, and saving the processed data to specified file paths.'''


# @dataclass #used for creating class variables and initializing them with default values
# class DataIngestionConfig:#this class is used to define the configuration for data ingestion, including the file paths for training data, testing data, and raw data.
#     train_data_path: str = os.path.join('artifacts', 'train.csv') #path to save the training data
#     test_data_path: str = os.path.join('artifacts', 'test.csv') #path to save the testing data
#     raw_data_path: str = os.path.join('artifacts', 'data.csv') #path to save the raw data
    

# class DataIngestion:
#     def __init__(self):
#         self.ingestion_config=DataIngestionConfig() #creating an instance of the DataIngestionConfig class to access the file paths for data ingestion
#     def initiate_data_ingestion(self):#this function is used for reading data
#         logging.info('entered the data ingestion method or component') #logging the entry into the data ingestion method
#         try:
#             current_dir = os.path.dirname(os.path.abspath(__file__))
#             project_root = os.path.dirname(os.path.dirname(current_dir))
#             data_path = os.path.join(project_root, 'notebook', 'data', 'stud.csv')
#             df = pd.read_csv(data_path)
#             logging.info('read the dataset as dataframe') #logging the successful reading of the dataset
            
#             os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) #creating the directory for saving the training data if it does not exist
#             df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True) #saving the raw data to the specified file path
            
#             logging.info('train test split initiated') #logging the initiation of the train-test split
#             train_set,test_set=train_test_split(df, test_size=0.2, random_state=42) #splitting the data into training and testing sets
#             train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True) #saving the training data to the specified file path
#             test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True) #saving the testing data to the specified file path
            
#             logging.info('ingestion of the data is completed') #logging the completion of the data ingestion process
#             return(
#                 self.ingestion_config.train_data_path, 
#                 self.ingestion_config.test_data_path
#                 )
#             #returning the file paths for the training and testing data 
#         except Exception as e:
#             raise CustomException(e, sys) #raising a custom exception if any error occurs during the data ingestion process
            
# if __name__=="__main__":    
#     obj=DataIngestion() #creating an instance of the DataIngestion class
#     train_data,tests_data=obj.initiate_data_ingestion() #initiating the data ingestion process
    
#     data_transformation=DataTransformation() #creating an instance of the DataTransformation class
#     data_transformation.initiate_data_transformation(train_data,tests_data) #initiating the data transformation process using the file paths for the training and testing data obtained from the data ingestion process



import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

# from src.components.model_trainer import ModelTrainerConfig
# from src.components.model_trainer import ModelTrainer
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.dirname(os.path.dirname(current_dir))
            data_path = os.path.join(project_root, 'notebook', 'data', 'stud.csv')
            df = pd.read_csv(data_path)
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    # modeltrainer=ModelTrainer()
    # print(modeltrainer.initiate_model_trainer(train_arr,test_arr))



