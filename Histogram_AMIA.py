import csv
import matplotlib.pyplot as plt

with open('C:\Users\prath\Desktop\WoundInf_Train_Labels.tsv','rb') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')
    tsvin.next()
    your_list = list(tsvin)

main_list = []
for i in range(0,len(your_list)):
    if your_list[i][1] == '1' or your_list[i][1] == '2':
        main_list.append(your_list[i])

dic_time = {'0-1': 0, '1-2':0, '2-3':0, '3-4':0, '4-5':0,'5-6':0,'6-':0}
count = 0
for i in range(0,len(main_list)):
    num = int(main_list[i][2].split()[0].split('-')[2])
    num2 = int(main_list[i][3].split()[0].split('-')[2])
    num_month = int(main_list[i][2].split()[0].split('-')[1])
    num2_month = int(main_list[i][3].split()[0].split('-')[1])
    num_year = int(main_list[i][2].split()[0].split('-')[0])
    num2_year = int(main_list[i][3].split()[0].split('-')[0])
    total_diff = (num2_year - num_year)*365+ (num2_month - num_month) * 30 + (num2 - num)

    if 0 <= total_diff <=7:
        dic_time['0-1'] = int(dic_time['0-1']) + 1
    elif 8 <= total_diff <= 14:
        dic_time['1-2'] = int(dic_time['1-2']) + 1
    elif 15 <= total_diff <= 21:
        dic_time['2-3'] = int(dic_time['2-3']) + 1
    elif 22 <= total_diff <= 28:
        dic_time['3-4'] = int(dic_time['3-4']) + 1
    elif 29 <= total_diff <= 35:
        dic_time['4-5'] = int(dic_time['4-5']) + 1
    elif 35 <= total_diff <= 42:
        dic_time['5-6'] = int(dic_time['5-6']) + 1
    else:
        dic_time['6-'] = int(dic_time['6-']) + 1


