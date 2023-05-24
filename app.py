import pickle
from flask import Flask,render_template,request
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from Src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            Age=request.form.get('Age'),
            Gender=request.form.get('Gender'),
            BMI=request.form.get("BMI"),
            Blood_pressure=request.form.get('Blood_pressure'),
            FBS=request.form.get("FBS"),
            HbA1c=request.form.get("HbA1c"),
            Family_History_of_Diabeties=request.form.get('Family_History_of_Diabeties'),
            Smoking=request.form.get('Smoking'),
            Diet=request.form.get('Diet'),
            Exercise=request.form.get('Exercise')
        )
        pred_df=data.get_data_as_df()
        print(pred_df)

        predict_pipeline=PredictPipeline()
        temp=predict_pipeline.predict(pred_df)
        if temp<0:
            results='Yes'
        else:
            results="No"
        return render_template('home.html',results=results)

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)

 