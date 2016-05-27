import pandas as pd
from pandas import DataFrame


a = pd.read_csv("C:\Users\prath\Desktop\Capstone\Data_Dcitionary.csv")
b = pd.read_csv("C:\Users\prath\Desktop\Capstone\WoundInf_Tests_Flattened_New.csv")
c = pd.read_csv("C:\Users\prath\Desktop\Capstone\WoundInf_Tests_Flattened.csv")
d = pd.read_csv("C:\Users\prath\Desktop\Capstone\AIMA_DATA.csv")

#Creating the no-result column: It is 0 when there is result, 1 otherwise
main_list = []

main_list.append(['PID', 'no-result'])
for i in range(0,len(c)):
    temp2 = []
    flag = False
    temp2.append(c['PID'][i])
    for j in range(0,len(b)):
        if c['PID'][i] == b['PID'][j]:
            flag = True
    if flag:
        temp2.append(0)
    else:
        temp2.append(1)
    main_list.append(temp2)

headers = main_list.pop(0)
df = DataFrame(main_list, columns=headers)

#Whole dataset
# b = pd.merge(b,df,how='outer')
# count_no = 0
# count_yes = 0
# for i in range(0,len(b)):
#     if b['no-result'][i] == 1:
#         count_no += 1
#     else:
#         count_yes += 1
#
# print count_yes
# print count_no

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

df1 = pd.merge(df1,df,on="PID",how='outer')
df1 = pd.merge(df1,d,on="PID")
df1 = df1.fillna(0)
print len(df1)
df1.to_csv("C:\Users\prath\Desktop\Capstone\TimeLine_Data.csv",index=False)