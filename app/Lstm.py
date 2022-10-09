import sklearn
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.preprocessing.sequence import TimeseriesGenerator
from app.Preprocessing import datacleaning
import os
from tensorflow import keras
#from tensorflow.keras.models import load_model
from config import *


def lstm(df):
    train = df.iloc[:29]
    test = df.iloc[29:]

    scaler = MinMaxScaler()
    scaler.fit(train)
    scaled_train = scaler.transform(train)
    scaled_test = scaler.transform(test)
    # define generator
    n_input = 2
    n_features = 1
    generator = TimeseriesGenerator(scaled_train, scaled_train, length=n_input, batch_size=1)
    X, y = generator[1]
    new_model = keras.models.load_model(load_model)
    new_model.predict(y)
    arr = new_model.predict(y)
    print(new_model.predict(y))



