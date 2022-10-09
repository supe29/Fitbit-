import requests
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from config import *


st.title("fitbit application")

menu = ["check calaries","Past Predictions"]
choice = st.sidebar.selectbox("Navigation", menu)

url = "http://127.0.0.1:8000/predict"

if choice == "check calaries":
        
        TotalSteps = st.text_input("TotalSteps", 0)
        TotalDistance = st.text_input("TotalDistance", 0)
        TrackerDistance = st.text_input("TrackerDistance", 0)
        WeightKg = st.text_input("WeightKg", 50)
        BMI = st.text_input("BMI", 22)
        
        myInput = {
        "TotalSteps" : TotalSteps,
        "TotalDistance" : TotalDistance,
        "TrackerDistance" : TrackerDistance,
        "WeightKg" : WeightKg,
        "BMI" : BMI
        }

        result=""
        if st.button("Predict"):
                prediction = requests.post(url, json=myInput)
                st.success('The Prediction is: '+prediction.text)

elif choice == "Past Predictions":
        #st.subheader("Past Predictions")
        opt = st.sidebar.selectbox("Predictions", ["Train Dataset", "Test Dataset"])   
        if opt == "Train Dataset":
                dailyactivity = pd.read_csv(fitbitdailyActivity_merged)
                dailycalories = pd.read_csv(fitdailyCalories_merged)
                heart = pd.read_csv(heartrate_seconds_merged)
                weight = pd.read_csv('C:/Users/kaust/fitbit/data/weightLogInfo_merged.csv') 
               
                chart_data = dailyactivity['Calories']

                df_steps = dailyactivity[['Id', 'ActivityDate', 'TotalSteps']]
                df_steps['ActivityDate'] = pd.to_datetime(df_steps['ActivityDate'])


                table = pd.pivot_table(df_steps, values='TotalSteps', index=['ActivityDate'],
                           columns=['Id'], aggfunc=np.sum, fill_value=0)


                dfactivity = dailyactivity.drop(
                ['LoggedActivitiesDistance', 'VeryActiveDistance', 'ModeratelyActiveDistance', 'LightActiveDistance', 'SedentaryActiveDistance', 'VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes', 'SedentaryMinutes']  , axis=1)
                dfall = pd.merge(dfactivity, weight, how='inner', left_on='Id', right_on='Id')
                dfall = dfall.drop(['Date', 'IsManualReport', 'LogId', 'Fat', 'Id'], axis=1)
                trail = dfall['Calories']
                st.line_chart(trail)
    
