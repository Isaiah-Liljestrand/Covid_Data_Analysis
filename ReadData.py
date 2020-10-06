# -*- coding: utf-8 -*-
import csv
import numpy as np
import matplotlib.pyplot as plt

filename = "owid-covid-data.csv"

fields = [] 
rows = []
mydict = None

with open(filename, 'r', encoding='utf') as csvfile: 
    csvreader = csv.reader(csvfile)
    fields = next(csvreader) 

    i = 0
    for row in csvreader: 
        rows.append(row)
        i += 1
        if i > 54:
            break
        
    mydict = csv.DictReader(csvfile)

    print("Total no. of rows: %d"%(csvreader.line_num)) 

print('Field names are:' + ', '.join(field for field in fields))