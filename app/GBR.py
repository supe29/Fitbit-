import sklearn
import pandas as pd 
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import tree
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
import pickle
from sklearn.model_selection import train_test_split
from app.Preprocessing import datacleaning
import os

print(os.getenv("DOMAIN"))

def train(df):
    X = df[['TotalSteps', 'TotalDistance', 'TrackerDistance', 'WeightKg', 'BMI']]
    y = df['Calories']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 / 3, random_state=0)


    crossvalidation = KFold(n_splits=10, shuffle=True, random_state=1)

    for depth in range(1, 10):
        tree_regressor = tree.DecisionTreeRegressor(max_depth=depth, random_state=1)
        if tree_regressor.fit(X, y).tree_.max_depth < depth:
            break
        score = np.mean(
            cross_val_score(tree_regressor, X, y, scoring='neg_mean_squared_error', cv=crossvalidation, n_jobs=1))

    model = pickle.load(open("models/GBR_pickle", "rb"))
    model.fit(X_train, y_train)
    arr = model.predict(X_test)
    score = np.mean(cross_val_score(model, X, y, scoring='neg_mean_squared_error', cv=crossvalidation, n_jobs=1))
    arr = arr.tolist()
    print(arr)
    print(score)
    return arr




