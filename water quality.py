# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:17:54 2019

@author: Adarsh kush
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import os

data= pd.read_csv('IndiaAffectedWaterQualityAreas.csv',encoding='latin1')

data.describe()

data['State Name'].unique()

data['Quality Parameter'].groupby(data['State Name']).describe()

import dateutil
data['date'] = data['Year'].apply(dateutil.parser.parse)
import datetime as dt
data['date'] = pd.to_datetime(data['date'])
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month
State_Data = data[['State Name', 'Quality Parameter']]
import sklearn
from sklearn.preprocessing import LabelEncoder
numbers = LabelEncoder()
State_Data['Quality'] = numbers.fit_transform(State_Data['Quality Parameter'])

State_Quality_Count = pd.DataFrame({'count' : State_Data.groupby( [ "State Name", "Quality","Quality Parameter"] ).size()}).reset_index()
State_Quality_Count

TAMIL_NADU = State_Quality_Count[State_Quality_Count["State Name"] == "TAMIL NADU"]
ANDHRA_PRADESH = State_Quality_Count[State_Quality_Count["State Name"] == "ANDHRA PRADESH"]
KERALA = State_Quality_Count[State_Quality_Count["State Name"] == "KERALA"]
KARNATAKA = State_Quality_Count[State_Quality_Count["State Name"] == "KARNATAKA"]
GUJARAT = State_Quality_Count[State_Quality_Count["State Name"] == "GUJARAT"]
MAHARASHTRA = State_Quality_Count[State_Quality_Count["State Name"] == "MAHARASHTRA"]
ASSAM = State_Quality_Count[State_Quality_Count["State Name"] == "ASSAM"]
UTTAR_PRADESH = State_Quality_Count[State_Quality_Count["State Name"] == "UTTAR PRADESH"]
UTTRAKHAND = State_Quality_Count[State_Quality_Count["State Name"] == "UTTRAKHAND"]
WEST_BENGAL = State_Quality_Count[State_Quality_Count["State Name"] == "WEST BENGAL"]
RAJASTHAN =  State_Quality_Count[State_Quality_Count["State Name"] == "RAJASTHAN"]
PUNJAB = State_Quality_Count[State_Quality_Count["State Name"] == "PUNJAB"]
ORISSA = State_Quality_Count[State_Quality_Count["State Name"] == "ORISSA"]
JAMMU_AND_KASHMIR = State_Quality_Count[State_Quality_Count["State Name"] == "JAMMU AND KASHMIR"]
HIMANCHAL_PRADESH = State_Quality_Count[State_Quality_Count["State Name"] == "HIMANCHAL_PRADESH"]
HARYANA = State_Quality_Count[State_Quality_Count["State Name"] == "HARYANA"]
CHATTISGARH = State_Quality_Count[State_Quality_Count["State Name"] == "CHATTISGARH"]
TRIPURA = State_Quality_Count[State_Quality_Count["State Name"] == "TRIPURA"]
MEGHALAYA = State_Quality_Count[State_Quality_Count["State Name"] == "MEGHALAYA"]
MANIPUR = State_Quality_Count[State_Quality_Count["State Name"] == "MANIPUR"]
JHARKHAND = State_Quality_Count[State_Quality_Count["State Name"] == "JHARKHAND"]



TAMIL_NADU
ASSAM
plt.figure(figsize=(6,4))
ax = sns.barplot(x="count", y ="Quality Parameter", data = GUJARAT)
ax.set(xlabel='Count')
sns.despine(left=True, bottom=True)
plt.title("Water Quality Parameter In Gujrat")