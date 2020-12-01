# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense

filename = "owid-covid-data.csv"

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
print(X_test.shape)

model = Sequential()
model.add(Dense(100, activation="relu", input_dim = X_train.shape[1]))
model.add(Dense(50, activation="relu"))
model.add(Dense(10, activation="relu"))
model.add(Dense(Y_train.shape[0], activation="softmax"))
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, Y_train, validation_data=(X_test, Y_test), verbose = 1, epochs = 20, shuffle=True)
predicted_valid_labels = np.argmax(model.predict(X_test), axis=1)
valid_labels = np.argmax(Y_test, axis=1)

test_range = len(valid_labels)
for k in range(0, test_range):
    if(predicted_valid_labels[k] == valid_labels[k]):
        sum = sum + 1
print("Accuracy = ", sum / test_range)
