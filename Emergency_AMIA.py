import csv
from datetime import datetime

with open('C:\Users\prath\Desktop\WoundInf_Train_Labels.tsv','rb') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')
    tsvin.next()
    your_list = list(tsvin)

print your_list

main_list = []
for i in range(0,len(your_list)):
    temp = []
    temp.append(your_list[i][0])
    d = datetime.strptime(your_list[i][2].split()[1], "%H:%M:%S")

    print your_list[i][2].split()[1]
    print d.strftime("%I")
    print d.strftime("%p")
    if (d.strftime("%p") == 'AM' and (int(d.strftime("%I")) < 06 or int(d.strftime("%I")) == 12)):
        temp.append(1)
    elif (d.strftime("%p") == 'PM' and (int(d.strftime("%I")) > 07 and int(d.strftime("%I")) != 12)):
        temp.append(1)
    else:
        temp.append(0)
    print temp
    main_list.append(temp)

with open("C:\Users\prath\Desktop\Capstone\AMIA_emergency.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(['PID', 'Emergency'])
    for item in main_list:
        writer.writerow(item)