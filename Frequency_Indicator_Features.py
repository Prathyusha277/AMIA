#Creating the frequency indicator features

import pandas as pd
import csv
import numpy as np
from collections import defaultdict

#Get all the tests that a patient had taken
a = pd.read_csv("B:\WoundInf_Train_Tests.tsv",sep='\t')

dictionary = {}
for i in range(0,len(a)):
    if dictionary.has_key(str(a['PID'][i])+'_'+str(a['TestType'][i])):
        dictionary[str(a['PID'][i])+'_'+str(a['TestType'][i])] += 1
    else:
        dictionary[str(a['PID'][i])+'_'+str(a['TestType'][i])] = 1

writer = csv.writer(open('C:\Users\prath\Desktop\Capstone\dict_data_temp.csv', 'wb')) #To make process faster storing the intermediate results
for key, value in dictionary.items():
    writer.writerow([key, value])

b = pd.read_csv("C:\Users\prath\Desktop\Capstone\dict_data_temp.csv")
dic_main = defaultdict(list)
for i in range(0,len(b)):
    pid = b.iloc[i][0].split('_')[0]
    fea = b.iloc[i][0].split('_')[1]
    count = b.iloc[i][1]
    temp = []
    temp.append(fea)
    temp.append(count)
    if dic_main.has_key(pid):
        dic_main[pid].append(temp)
    else:
        dic_main[pid].append(temp)

#Create a dataset with 130 features as columns
with open('C:\Users\prath\Desktop\Capstone\Data_Dcitionary.csv', 'rb') as f: #AMIA data dictionary
    reader = csv.reader(f)
    next(reader, None)
    your_list1 = list(reader)

mainlist = []
mainlist.append('PID')

for i in range(0,len(your_list1)):
    if your_list1[i][1] == '1':
        mainlist.append(your_list1[i][0])

#creating an empty dataframe with columns and filling it later
df = pd.DataFrame(np.full((len(dic_main), len(mainlist)), np.nan),columns=mainlist)

for i in range(0,len(dic_main)):
    pid = dic_main.keys()[i]
    print pid
    fea_list = dic_main[pid]
    print fea_list
    df['PID'][i] = int(pid)
    for j in range(0,len(fea_list)):
        print fea_list[j][0]
        string = str(fea_list[j][0]).replace("'","")
        if string in df:
            print string
            df[string][i] = fea_list[j][1]

df = df.fillna(0)
df.to_csv("C:\Users\prath\Desktop\Capstone\Frequency_Indicator_Features.csv")


