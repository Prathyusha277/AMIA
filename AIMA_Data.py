import csv

with open('B:\WoundInf_Train_Labels.tsv','rb') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')
    tsvin.next()
    your_list = list(tsvin)

list = []
list =  your_list[0][2].split("-")
print list[0]

for i in range(0,len(your_list)):
    if your_list[i][1] == '1' or your_list[i][1] == '2':
        your_list[i][1] = '1'
    else:
        your_list[i][1] = '0'
    if your_list[i][4] == 'M':
        your_list[i][4] = '1'
    elif your_list[i][4] == 'F':
        your_list[i][4] = '2'
    list = your_list[i][2].split("-")
    difference = int(list[0]) - int(your_list[i][5])
    your_list[i].append(difference)
    print your_list[i]

with open("C:\Users\prath\Desktop\Capstone\AIMA_DATA.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(['PID', 'Infection', 't.IndexSurgery', 't.Infection', 'Sex', 'YoB', 'ageAtSurgery'])
    for item in your_list:
        writer.writerow(item)
