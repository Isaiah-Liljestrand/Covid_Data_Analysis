# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential, Model
from keras.layers import Dense, Input

filename = "owid-covid-data-new.csv"

data = pd.read_csv(filename)

for (columnName, columnData) in data.iteritems():
    newstring = columnName + ": "
    count = 0
    for i, item in enumerate(columnData):
        if pd.notnull(item):
            count += 1
    print(newstring + "\t" + str(count) + "/" + str(len(columnData)) + "\t(" + str(len(columnData) - count) + ") are null")

selecteddata = data[["total_cases", "new_cases", "total_deaths", "new_deaths", "stringency_index", "population", "population_density", "median_age", "aged_65_older", "aged_70_older", "gdp_per_capita", "cardiovasc_death_rate", "diabetes_prevalence", "hospital_beds_per_thousand", "life_expectancy", "human_development_index"]]
print(len(selecteddata["total_cases"]) - sum(selecteddata.isnull().any(axis=1)))
perfectdata = selecteddata[-selecteddata.isnull().any(axis=1)]

print(perfectdata)
Y = perfectdata.pop("total_deaths")

X_train, X_test, Y_train, Y_test = train_test_split(perfectdata, Y, test_size = 0.2)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

input_layer = Input(shape=(perfectdata.shape[1],))
dense_layer_1 = Dense(100, activation='relu')(input_layer)
dense_layer_2 = Dense(50, activation='relu')(dense_layer_1)
dense_layer_3 = Dense(25, activation='relu')(dense_layer_2)
output = Dense(1)(dense_layer_3)

model = Model(inputs=input_layer, outputs=output)
model.compile(loss="mean_squared_error" , optimizer="adam", metrics=["mean_squared_error"])

history = model.fit(X_train, Y_train, batch_size=2, epochs=100, verbose=1, validation_split=0.2)
