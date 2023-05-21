import os,sys
from Src.exception import CustomException
from Src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataingestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self) -> None:
        self.data_ingestion_config=DataingestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Enter the Data Ingestion Method")
        try:
            df=pd.read_csv('notebook\Diabetes Classification.csv')
            logging.info("Read the Dataset as Dataframe")

            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path))

            df.to_csv(self.data_ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train Test Split has been initited")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=2)

            train_set.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of the data has been Complted")

            return (self.data_ingestion_config.train_data_path,self.data_ingestion_config.test_data_path)
        
        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()