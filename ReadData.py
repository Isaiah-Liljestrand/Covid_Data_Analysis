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