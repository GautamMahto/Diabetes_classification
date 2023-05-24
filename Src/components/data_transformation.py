# import os,sys
# from dataclasses import dataclass
# import numpy as np
# import pandas as pd
# from sklearn.compose import ColumnTransformer
# from sklearn.impute import SimpleImputer
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import OneHotEncoder,StandardScaler

# from Src.exception import CustomException
# from Src.logger import logging
# from Src.utils import save_object

# @dataclass
# class DataTransformationConfig:
#     preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

# class DataTransformation:
#     def __init__(self) -> None:
#         self.data_transformation_config=DataTransformationConfig()
    
#     def get_data_transformer_object(self):
#         logging.info("Data Transformation has been Started")
#         try:
#             numerical_columns=['Age','BMI','FBS','HbA1c']
#             categorical_columns=['Gender','Blood Pressure','Family History of Diabetes','Smoking','Diet','Exercise']

#             num_pipeline=Pipeline(
#                 steps=[
#                     ("imputer",SimpleImputer(strategy="median")),
#                     ("scaler",StandardScaler())
#                 ]
#             )
#             logging.info("Numerical Encoding has been done")
#             cat_pipeline=Pipeline(
#                 steps=[
#                     ("imputer",SimpleImputer(strategy="most_frequent")),
#                     ("one_hot_encoder",OneHotEncoder()),
#                     ("scaler",StandardScaler(with_mean=False))

#                 ]
#             )
#             logging.info("Categorical Encoding(Columns) has been done")

#             preprocessor=ColumnTransformer(
#                 [
#                     ("num_pipeline",num_pipeline,numerical_columns),
#                     ("cat_pipelines",cat_pipeline,categorical_columns) 
#                  ]
#             )

#             return preprocessor

#         except Exception as e:
#             raise CustomException(e,sys)
#     def initiate_data_transformation(self,train_path,test_path):
#         try:
#             train_df=pd.read_csv(train_path)
#             test_df=pd.read_csv(test_path)

#             logging.info("Read Train and test Data path")

#             logging.info("Obtaining Preprocessor object")

#             preprocessing_object=self.get_data_transformer_object()

#             target_column_name="Diagnosis"

#             input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
#             target_feature_train_df=train_df[target_column_name]

#             input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
#             target_feature_test_df=test_df[target_column_name]

#             input_feature_train_arr=preprocessing_object.fit_transform(input_feature_train_df)
#             input_feature_test_arr=preprocessing_object.transform(input_feature_test_df)

#             train_arr=np.c_[
#                 input_feature_train_arr,np.array(target_feature_train_df)
#             ]

#             test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

#             logging.info("Saved preprocessing object.")

#             save_object(
#                 file_path=self.data_transformation_config.preprocessor_obj_file_path,
#                 obj=preprocessing_object
#             )

#             return (
#                 train_arr,test_arr,self.data_transformation_config.preprocessor_obj_file_path
#             )

#         except Exception as e:
#             raise CustomException(e,sys)



# code after the target one


import os,sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from Src.exception import CustomException
from Src.logger import logging
from Src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self) -> None:
        self.data_transformation_config=DataTransformationConfig()
    
    def get_data_transformer_object(self):
        logging.info("Data Transformation has been Started")
        try:
            numerical_columns=['Age','BMI','FBS','HbA1c']
            categorical_columns=['Gender','Blood Pressure','Family History of Diabetes','Smoking','Diet','Exercise','Diagnosis']

            num_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                ]
            )
            logging.info("Numerical Encoding has been done")
            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))

                ]
            )
            logging.info("Categorical Encoding(Columns) has been done")

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

            logging.info("Read Train and test Data path")

            logging.info("Obtaining Preprocessor object")

            preprocessing_object=self.get_data_transformer_object()

            target_column_name="Diagnosis"

            input_feature_train_df=train_df
            # target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df
            # target_feature_test_df=test_df[target_column_name]

            input_feature_train_arr=preprocessing_object.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_object.transform(input_feature_test_df)

            train_arr=np.c_[
                input_feature_train_arr  #,np.array(target_feature_train_df)
            ]

            test_arr=np.c_[input_feature_test_arr ] # ,np.array(target_feature_test_df)
                           

            logging.info("Saved preprocessing object.")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_object
            )

            return (
                train_arr,test_arr,self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomException(e,sys)
