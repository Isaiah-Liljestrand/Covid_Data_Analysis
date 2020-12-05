# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential, Model
from keras.layers import Dense, Input
from numpy.random import randint
from statistics import median, mean


filename = "owid-covid-data-new.csv"

data = pd.read_csv(filename)

selecteddata = data[["total_cases", "new_cases", "total_deaths", "new_deaths", "stringency_index", "population", "population_density", "median_age", "aged_65_older", "aged_70_older", "gdp_per_capita", "cardiovasc_death_rate", "diabetes_prevalence", "hospital_beds_per_thousand", "life_expectancy", "human_development_index"]]
print(len(selecteddata["total_cases"]) - sum(selecteddata.isnull().any(axis=1)))
perfectdata = selecteddata[-selecteddata.isnull().any(axis=1)]
scaler = StandardScaler()
Y = perfectdata.pop("total_deaths")
accuracylist = list()

layer1 = [50, 75, 100, 150, 200, 250, 300, 400]
layer2 = [25, 50, 75, 100, 125, 150, 175, 200]
layer3 = [10, 20, 30, 40, 50, 60, 70, 80]

for i in range(8):
    for j in range(10):
        print("\n\n\nConfiguration ", i, " run ", j)
        X_train, X_test, Y_train, Y_test = train_test_split(perfectdata, Y, test_size = 0.2, random_state=42)
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        input_layer = Input(shape=(perfectdata.shape[1],))
        dense_layer_1 = Dense(layer1[i], activation='relu')(input_layer)
        dense_layer_2 = Dense(layer2[i], activation='relu')(dense_layer_1)
        dense_layer_3 = Dense(layer3[i], activation='relu')(dense_layer_2)
        output = Dense(1)(dense_layer_3)

        model = Model(inputs=input_layer, outputs=output)
        model.compile(loss="mean_squared_error" , optimizer="adam", metrics=["mean_squared_error"])

        history = model.fit(X_train, Y_train, epochs=80, verbose=1, validation_split=0.2)

        mean_squared_error = model.evaluate(X_test, Y_test, verbose=1)
        accuracylist.append(mean_squared_error[0])
tmplist = list()
meanlist = list()
medianlist = list()
for i in range(8):
    for j in range(10):
        tmplist.append(accuracylist[(i * 10) + j])
    meanlist.append(mean(tmplist))
    medianlist.append(median(tmplist))
    tmplist.clear()
print("Finished")
print("Full list:")
print(accuracylist)
print("\nMeans:")
print(meanlist)
print("\nMedians:")
print(medianlist)
