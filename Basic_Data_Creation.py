import csv

with open('B:\WoundInf_Train_Labels.tsv','rb') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')
    tsvin.next()
    your_list = list(tsvin)

with open('C:\Users\prath\Desktop\Capstone\WoundInf_Tests_Flattened.csv', 'rb') as f:
    reader = csv.reader(f)
    next(reader, None)
    your_list1 = list(reader)

print your_list1[2]
main_list = []

for i in range(0,len(your_list)):
    list = []
    list.append(your_list[i][0])
    if your_list[i][1] == '1' or your_list[i][1] == '2':
        list.append(1)
    else:
        list.append(0)
    if your_list[i][4] == 'M':
        list.append(1)
    elif your_list[i][4] == 'F':
        list.append(2)
    temp = your_list[i][2].split("-")
    difference = int(temp[0]) - int(your_list[i][5])
    list.append(difference)
    for j in range(1,len(your_list1)):
        if your_list[i][0] == your_list1[j][1]:
            list.append(your_list1[j][len(your_list1[j])-1])
            break
    main_list.append(list)

print main_list

with open("C:\Users\prath\Desktop\Capstone\AIMA_DATA.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(['PID', 'Infection', 'Sex', 'ageAtSurgery', 'NumberOfTestsTaken'])
    for item in main_list:
        writer.writerow(item)
