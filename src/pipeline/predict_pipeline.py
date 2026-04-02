import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
# from src.logger import logging


class PredictionPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            # model_path='artifacts/model.pkl'
            # preprocessor_path='artifacts/preprocessor.pkl'
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            
            # 2. USE the variable to build the full path
            model_path = os.path.join(project_root, 'artifacts', 'model.pkl')
            preprocessor_path = os.path.join(project_root, 'artifacts', 'preprocessor.pkl')
            # model_path = os.path.join(project_root, 'artifacts', 'model.pkl')
            # preprocessor_path = os.path.join(project_root, 'artifacts', 'preprocessor.pkl')
            #loading the model and preprocessor objects
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            pred=model.predict(data_scaled)
            return pred
        except Exception as e:
            raise CustomException(e, sys)
    


#for mapping html form data to the dataclass
class CustomData:
    def __init__(self,
                 gender:str,
                 race_ethnicity:str,
                 parental_level_of_education:str,
                 lunch:str,
                 test_preparation_course:str,
                 reading_score:int,
                 writing_score:int):
        self.gender=gender
        self.race_ethnicity=race_ethnicity
        self.parental_level_of_education=parental_level_of_education
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score
  
#this function will return the data in the form of dataframe which will be used for prediction  
#imputs from the web app will map to these values in the dicitonary and then converted to dataframe    
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = { 
            "gender":[self.gender],
            "race_ethnicity":[self.race_ethnicity],
            "parental_level_of_education":[self.parental_level_of_education],
            "lunch":[self.lunch],
            "test_preparation_course":[self.test_preparation_course],
            "reading_score":[self.reading_score],
            "writing_score":[self.writing_score]
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)