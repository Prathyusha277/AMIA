#Filtering Annie's features from the data

import pandas as pd

a = pd.read_csv("C:\Users\prath\Desktop\Capstone\Data_Dcitionary.csv") #This is the AMIA Data dictionary file
b = pd.read_csv("C:\Users\prath\Desktop\Capstone\WoundInf_Tests_Flattened.csv") #Flattened data created from "Flatten_Data.R" file
d = pd.read_csv("C:\Users\prath\Desktop\Capstone\AIMA_DATA.csv") #File created from "Basic_Data_Creation.py" file

#get only Annie's features
temp = []
for i in range(0,len(a)):
    if a.iloc[i,1] == 1.0:
        temp.append(a.iloc[i,0])

df1 = pd.DataFrame()
df1['PID'] = b['PID']
for i in range(0,len(temp)):
    if temp[i] + '_Mean' in b:
        df1[temp[i] + '_Mean'] = b[temp[i] + '_Mean']
    if temp[i] + '_Max' in b:
        df1[temp[i] + '_Max'] = b[temp[i] + '_Max']
    if temp[i] + '_Min' in b:
        df1[temp[i] + '_Min'] = b[temp[i] + '_Min']
    if temp[i] + '_SD' in b:
        df1[temp[i] + '_SD'] = b[temp[i] + '_SD']

#Merge with basic data which is in data frame "d"
df1 = pd.merge(df1,d,on="PID")
df1.to_csv("C:\Users\prath\Desktop\Capstone\TimeLine_Data_Annie.csv",index=False)