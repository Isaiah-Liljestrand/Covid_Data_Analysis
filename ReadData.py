# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = "owid-covid-data.csv"

data = pd.read_csv(filename)
# iterating the columns 
for col in data.columns: 
    print(col)