# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = "owid-covid-data.csv"

data = pd.read_csv(filename)

for (columnName, columnData) in data.iteritems():
    newstring = columnName + ": "
    count = 0
    for i, item in enumerate(columnData):
        if pd.notnull(item):
            count += 1
    print(newstring + "\t" + str(count) + "/" + str(len(columnData)) + "\t(" + str(len(columnData) - count) + ") are null")
    
selecteddata = data[["iso_code", "continent", "location", "date", "total_cases", "new_cases", "total_deaths", "new_deaths", "stringency_index", "population", "population_density", "median_age", "aged_65_older", "aged_70_older", "gdp_per_capita", "cardiovasc_death_rate", "diabetes_prevalence", "hospital_beds_per_thousand", "life_expectancy", "human_development_index"]]
print(len(selecteddata["iso_code"]) - sum(selecteddata.isnull().any(axis=1)))
perfectdata = selecteddata[-selecteddata.isnull().any(axis=1)]