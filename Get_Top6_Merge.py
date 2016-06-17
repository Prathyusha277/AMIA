#Get top 6 features from data set and merge those with the frequency indicator features

import pandas as pd
import csv
import numpy as np

a = pd.read_csv("C:\Users\prath\Desktop\Capstone\TimeLine_Data_Final_MissingFilled.csv") #File created from "Fill_MissingValues.py"
b = pd.read_csv("C:\Users\prath\Desktop\Capstone\Frequency_Indicator_Features.csv") #File created from "Frequency_Indicator_Features.py"
c = pd.read_csv("C:\Users\prath\Desktop\Capstone\AIMA_DATA.csv") #Basic data file

#Get all 92 features (Ignore the features with 1 as the number patients)
with open('C:\Users\prath\Desktop\Capstone\Patient_count_New.csv', 'rb') as f:
    reader = csv.reader(f)
    next(reader, None)
    your_list = list(reader)

main_list = []
for i in range(0,len(your_list)):
    if int(your_list[i][3]) > 1:
        main_list.append(your_list[i])

print len(main_list)
#Get min/max/sd/mean of top 6(>500 patients) features
df = pd.DataFrame()
for i in range(0,len(main_list)):
    df['PID'] = a[['PID']]
    if int(main_list[i][3]) >= 500:
        df[main_list[i][0]+'_Max'] = a[[main_list[i][0]+'_Max']]
        df[main_list[i][0]+'_Min'] = a[[main_list[i][0] + '_Min']]
        df[main_list[i][0]+'_Mean'] = a[[main_list[i][0] + '_Mean']]
        df[main_list[i][0]+'_SD'] = a[[main_list[i][0] + '_SD']]

#Get only the 92 features from the dataframe "b"
df1 = pd.DataFrame()
for i in range(0,len(main_list)):
    df1['PID'] = b[['PID']]
    df1[main_list[i][0]] = b[main_list[i][0]]

df = pd.merge(df,df1, on='PID')
df = pd.merge(df,c, on='PID')
df = df.iloc[np.random.permutation(len(df))]
print len(df.columns)

df.to_csv("C:\Users\prath\Desktop\Capstone\TimeLine_Data_Final.csv")
