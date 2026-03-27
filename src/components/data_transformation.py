# #feature engineering, conversion of data
# import sys
# from dataclasses import dataclass
# import os
# import numpy as np
# import pandas as pd
# from sklearn.base import BaseEstimator, TransformerMixin
# from sklearn.compose import ColumnTransformer
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import StandardScaler, OneHotEncoder
# from sklearn.impute import SimpleImputer
# # from src.components.data_ingestion import DataIngestion
# from src.exception import CustomException
# from src.logger import logging
# from src.utils import save_object
# '''the data transformation component is responsible 
# for performing feature engineering and data transformation 
# tasks. It includes a custom transformer class, 
# FeatureGenerator, which inherits from BaseEstimator 
# and TransformerMixin. This class is designed to generate 
# new features based on existing features in the dataset. 
# The DataTransformation class is responsible for applying the feature 
# generation process to the training and testing data, 
# and saving the transformed data to specified file paths.'''


# class DataTranformationConfig:  # this class is used to define the configuration for data transformation, including the file path to save the preprocessor object using pickle.
#     preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')  # file path to save the preprocessor object using pickle

# # why is preprocessor object used?
# # The preprocessor object is used to save the data transformation
# # pipeline, which includes the steps for handling missing values
# # scaling numerical features, and encoding categorical features.
# # By saving the preprocessor object, we can reuse the same data
# # transformation steps during both training and testing phases, 
# # ensuring consistency in the data processing. This is particularly 
# # important when deploying the model, as it allows us to apply the 
# # same transformations to new incoming data before making predictions.


# class DataTransformation:
#     def __init__(self):
#         self.data_transformation_config = DataTranformationConfig()  # creating an instance of the DataTranformationConfig class to access the file path for saving the preprocessor object

#     def get_data_transformer_object(self):  # this function is used to create and return a data transformer object, which includes a pipeline for numerical and categorical feature transformation.
#         try:
#             num_cols = ['writing score', 'reading score']  # list of numerical columns in the dataset
#             categorical_cols = ['gender', 'race', 'parental_level of education', 'lunch', 'test_preparation_course']  # list of categorical columns in the dataset

#             num_pipeline = Pipeline(
#                 steps=[
#                     ('imputer', SimpleImputer(strategy='median')),  # step for handling missing values in numerical features using median imputation
#                     ('scaler', StandardScaler())  # step for scaling numerical features using standardization
#                 ]
#             )

#             cat_pipelien = Pipeline(
#                 steps=[
#                     ('imputer', SimpleImputer(strategy='most_frequent')),  # step for handling missing values in categorical features using most frequent imputation
#                     ('one_hot_encoder', OneHotEncoder()),  # step for encoding categorical features using one-hot
#                     ('scaler', StandardScaler())  # step for scaling the encoded categorical features using standardization without centering
#                 ]
#             )

#             logging.info('numerical  pipeline is created')  # logging the successful creation of the numerical and categorical pipelines
#             logging.info('categorial pipeline is created')

#             preprocessor = ColumnTransformer(
#                 [
#                     ('num_pipeline', num_pipeline, num_cols),  # applying the numerical pipeline to the specified numerical columns
#                     ('cat_pipeline', cat_pipelien, categorical_cols)  # applying the categorical pipeline to the specified categorical columns
#                 ]
#             )

#             return preprocessor  # returning the preprocessor object that includes the combined numerical and categorical pipelines
#         except Exception as e:
#             raise CustomException(e, sys)  # raising a custom exception if any error occurs during the creation of the data transformer object
        
        
        
#     def initiate_data_transformation(self,train_path,test_path):
#         try:
#             train_df = pd.read_csv(train_path)  # reading the training data from the specified file path
#             test_df = pd.read_csv(test_path)  # reading the testing data from the specified file path
#             logging.info('read train and test data completed')  # logging the successful reading of the training and testing data

#             logging.info('obtaining preprocessor object')  # logging the initiation of obtaining the preprocessor object
#             preprocessor_obj = self.get_data_transformer_object()  # obtaining the preprocessor object by calling the get_data_transformer_object function

#             target_column_name = 'math_score'  # defining the target column name for the dataset
#             input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)  # separating the input features from the target variable in the training data
#             target_feature_train_df = train_df[target_column_name]  # extracting the target variable from the training data

#             input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)  # separating the input features from the target variable in the testing data
#             target_feature_test_df = test_df[target_column_name]  # extracting the target variable from the testing data

#             logging.info('applying preprocessing object on training and testing dataframe')  # logging the initiation of applying the preprocessor object to the training and testing data
#             input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)  # applying the preprocessor object to fit and transform the input features of the training data
#             input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)  # applying the preprocessor object to transform the input features of the testing data
            
#             #NP._C is used to concatenate the transformed input features with the target variable for both the training and testing data, creating new arrays that include both the features and the target variable for further processing in machine learning models.
#             train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]  # combining the transformed input features with the target variable for the training data
#             test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]  # combining the transformed input features with the target variable for the testing data

#             logging.info('saved preprocessing object')  # logging the successful saving of the preprocessor object using pickle
#             save_object(
#                 file_path=self.data_transformation_config.preprocessor_obj_file_path,  # file path to save the preprocessor object
#                 obj=preprocessor_obj  # preprocessor object to be saved using pickle
#             )               
#             return (
#                 train_arr,  # returning the transformed training data as a numpy array
#                 test_arr,  # returning the transformed testing data as a numpy array
#                 self.data_transformation_config.preprocessor_obj_file_path  # returning the file path where the preprocessor object is saved
#             )
#         except Exception as e:
#             raise CustomException(e, sys)  # raising a custom exception if any error occurs during the data transformation process
        
    
# # if __name__=="__main__":
# #     train_path, test_path = DataIngestion().initiate_data_ingestion()  # initiating the data ingestion process to obtain the file paths for the training and testing data
# #     DataTransformation().initiate_data_transformation(train_path, test_path)  # initiating the data transformation process using the obtained file paths for the training and testing data




import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function si responsible for data trnasformation
        
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())

                ]
            )

            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
                ]

            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)

                ]


            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()

            target_column_name="math_score"
            numerical_columns = ["writing_score", "reading_score"]

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
