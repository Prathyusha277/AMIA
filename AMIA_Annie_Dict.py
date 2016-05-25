# # -*- coding: utf-8 -*-
import csv
import pandas as pd

a = pd.read_csv("C:\Users\prath\Desktop\Capstone\Data_Dcitionary.csv")
b = pd.read_csv("C:\Users\prath\Desktop\Capstone\WoundInf_Tests_Flattened.csv")
temp = []
d  = []
for i in range(0,len(a)):
    if a.iloc[i,1] == 1.0:
        temp.append(a.iloc[i,0])

df = pd.DataFrame()
df['PID'] = b['PID']
for i in range(0,len(temp)):
    df[temp[i]+'_Mean'] = b[temp[i]+'_Mean']
    df[temp[i] + '_SD'] = b[temp[i] + '_SD']

print list(df.columns.values)

df.to_csv("C:\Users\prath\Desktop\Capstone\Data_Dict.csv")