import numpy as np
import pandas as pd
import pickle
from pathlib import Path
from streamlit.delta_generator import DeltaGenerator as _DeltaGenerator
from streamlit import cursor
from streamlit.type_util import ValueFieldName
import pyarrow as pa
import pyarrow.lib as _lib


def datacleaning(dailyactivity, weight):
    print(dailyactivity.head())
    df_steps = dailyactivity[['Id', 'ActivityDate', 'TotalSteps']]
    df_steps['ActivityDate'] = pd.to_datetime(df_steps['ActivityDate'])


    table = pd.pivot_table(df_steps, values='TotalSteps', index=['ActivityDate'],
                           columns=['Id'], aggfunc=np.sum, fill_value=0)


    dfactivity = dailyactivity.drop(
        ['LoggedActivitiesDistance', 'VeryActiveDistance', 'ModeratelyActiveDistance', 'LightActiveDistance',
         'SedentaryActiveDistance', 'VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes',
         'SedentaryMinutes']
        , axis=1)


    dfid81 = table.drop([1503960366, 1644430081, 1844505072, 1927972279,
                         2022484408, 2026352035, 2320127002, 2347167796, 2873212765,
                         3372868164, 3977333714, 4020332650, 4057192912, 4319703577,
                         4388161847, 4445114986, 4558609924, 4702921684, 5553957443,
                         5577150313, 6117666160, 6290855005, 6775888955, 6962181067,
                         7007744171, 7086361926, 8053475328, 8253242879, 8378563200,
                         8583815059, 8792009665, 8877689391]
                        , axis=1)

    dfall = pd.merge(dfactivity, weight, how='inner', left_on='Id', right_on='Id')
    dfall = dfall.drop(['Date', 'IsManualReport', 'LogId', 'Fat', 'Id'], axis=1)
    return dfall,dfid81










