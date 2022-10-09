
import pandas as pd
from app.Preprocessing import datacleaning
from app.GBR import train
from app.Lstm import lstm
import streamlit as st
from config import *



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dailyactivity = pd.read_csv(fitbitdailyActivity_merged)
    dailycalories = pd.read_csv(fitdailyCalories_merged)
    heart = pd.read_csv(heartrate_seconds_merged)
    weight = pd.read_csv('C:/Users/kaust/fitbit/data/weightLogInfo_merged.csv')
    df,df81=datacleaning(dailyactivity, weight)
    train_df=train(df)
    train2=lstm(df81)
