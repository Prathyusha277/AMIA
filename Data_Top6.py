import pandas as pd
import csv
import numpy as np

a = pd.read_csv("C:\Users\prath\Desktop\Capstone\TimeLine_Data_Annie_MissingFilled_zero.csv")
b = pd.read_csv("C:\Users\prath\Desktop\Capstone\dict_main_temp_new.csv")
c = pd.read_csv("C:\Users\prath\Desktop\Capstone\AIMA_DATA.csv")

#Get all 92 features
with open('C:\Users\prath\Desktop\Capstone\Patient_count_1.csv', 'rb') as f:
    reader = csv.reader(f)
    next(reader, None)
    your_list = list(reader)

main_list = []
for i in range(0,len(your_list)):
    if int(your_list[i][1]) > 1:
        main_list.append(your_list[i])

#Get min/max/sd/mean of top 6(>500 patients) features
df = pd.DataFrame()
for i in range(0,len(main_list)):
    df['PID'] = a[['PID']]
    if int(main_list[i][1]) > 500:
        df[main_list[i][0]+'_Max'] = a[[main_list[i][0]+'_Max']]
        df[main_list[i][0]+'_Min'] = a[[main_list[i][0] + '_Min']]
        df[main_list[i][0]+'_Mean'] = a[[main_list[i][0] + '_Mean']]
        df[main_list[i][0]+'_SD'] = a[[main_list[i][0] + '_SD']]

#Get only the 92 features from the dataframe a
df1 = pd.DataFrame()
for i in range(0,len(main_list)):
    df1['PID'] = b[['PID']]
    df1[main_list[i][0]] = b[main_list[i][0]]

df = pd.merge(df,df1, on='PID')
df = pd.merge(df,c, on='PID')
df = df.iloc[np.random.permutation(len(df))]

df.to_csv("C:\Users\prath\Desktop\Capstone\TimeLine_Data_Final_missing_0.csv")

