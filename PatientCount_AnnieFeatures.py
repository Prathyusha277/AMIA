#Counting number of patients who had taken a particular blood test

import csv
import pandas as pd

a = pd.read_csv("C:\Users\prath\Desktop\Capstone\Data_Dcitionary.csv") #AMIA Data dictionary
with open('C:\Users\prath\Desktop\Capstone\Timeline_Data_Annie.csv', 'rb') as f: #File created from "Timeline_Data.py"
    reader = csv.reader(f)
    your_list = list(reader)

#3 dictionaries to store the number of infected, non-infected and total patients for all blood test
count = {}
count_infec = {}
count_noninfec = {}
for i in range(1,len(your_list)-1):
    for j in range(1,len(your_list[i])):
        if your_list[i][j] != '':
            if count.has_key(your_list[0][j]):
                count[your_list[0][j]] += 1
            else:
                count[your_list[0][j]] = 1
        if your_list[i][j] != '' and your_list[i][len(your_list[i])-1] == '1':
            if count_infec.has_key(your_list[0][j]):
                count_infec[your_list[0][j]] += 1
            else:
                count_infec[your_list[0][j]] = 1
        if your_list[i][j] != '' and your_list[i][len(your_list[i])-1] == '0':
            if count_noninfec.has_key(your_list[0][j]):
                count_noninfec[your_list[0][j]] += 1
            else:
                count_noninfec[your_list[0][j]] = 1

#get Annie's features
temp = []
for i in range(0,len(a)):
    if a.iloc[i,1] == 1.0:
        temp.append(a.iloc[i,0])

#Assigning the count to each feature
count_list = []
for i in range(0,len(temp)):
    if count.has_key(temp[i] + '_Mean'):
        temp1 = []
        temp1.append(temp[i])

        if count_noninfec.has_key(temp[i] + '_Mean'):
            temp1.append(count_noninfec[temp[i] + '_Mean'])
        else:
            temp1.append(0)
        if count_infec.has_key(temp[i] + '_Mean'):
            temp1.append(count_infec[temp[i] + '_Mean'])
        else:
            temp1.append(0)

        temp1.append(count[temp[i] + '_Mean'])
        count_list.append(temp1)

#Sorting the data based on the total patient count
count_list.sort(key=lambda x: x[3],reverse=True)

with open("C:\Users\prath\Desktop\Capstone\Patient_count_New.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(['Feature','Non-infected','Infected','Total'])
    for item in count_list:
        writer.writerow(item)