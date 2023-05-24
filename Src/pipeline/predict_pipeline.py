import os ,sys
import pandas as pd
import numpy as np
from Src.exception import CustomException
from Src.utils import load_object

class PredictPipeline:
    def __init__(self) -> None:
        pass

    def predict(self,features):
        try:
            model_path='artifacts\model.pkl'
            preprocessor_path='artifacts\preprocessor.pkl'

            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)

            return preds
        except Exception as e:
            raise CustomException(e,sys)

class CustomData:
    def __init__(self,Age:int,Gender:str,BMI:int,Blood_pressure:str,FBS:int,HbA1c:int,Family_History_of_Diabeties:str,Smoking:str,Diet:str,Exercise:str):
        self.Age=Age
        self.Gender=Gender
        self.BMI=BMI
        self.Blood_pressure=Blood_pressure
        self.FBS=FBS
        self.HbA1c=HbA1c
        self.Family_History_of_Diabeties=Family_History_of_Diabeties
        self.Smoking=Smoking
        self.Diet=Diet
        self.Exercise=Exercise
    
    def get_data_as_df(self):
        try:
            custom_data_input_dict={
                "Age":[self.Age],
                "Gender":[self.Gender],
                "BMI":[self.BMI],
                "Blood_pressure":[self.Blood_pressure],
                "FBS":[self.FBS],
                "HbA1c":[self.HbA1c],
                "Family_History_of_Diabeties":[self.Family_History_of_Diabeties],
                "Smoking":[self.Smoking],
                "Diet":[self.Diet],
                "Exercise":[self.Exercise]
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)