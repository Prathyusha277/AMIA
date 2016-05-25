# -*- coding: utf-8 -*-
import csv
import xlwt
from tempfile import TemporaryFile
#
with open('B:\WoundInf_Train_Tests.tsv','rb') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')
    tsvin.next()
    your_list = list(tsvin)

dic = []
temp = []
for i in range(0,len(your_list)):
    temp.append(your_list[i][2].decode('utf8'))

dic = list(set(temp))


book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')

for i,e in enumerate(dic):
    sheet1.write(i,1,e)

name = "C:\Users\prath\Desktop\Capstone\srandom.xls"
book.save(name)
book.save(TemporaryFile())

# with open("C:\Users\prath\Desktop\Capstone\AMIA_Tests1.csv", "wb") as f:
#     writer = csv.writer(f)
#     writer.writerow(['Test Name'])
#     for item in dic:
#         writer.writerow([item])
# for i in range(0,len(dic)):
#     print dic[i]
#     myString = ",".join(dic)

# import openpyxl
# import xlwt
# from tempfile import TemporaryFile
#
# wb = openpyxl.load_workbook('C:\Users\prath\Desktop\WoundInf_Train_Tests.xlsx')
# sheet = wb.get_sheet_by_name('WoundInf_Train_Tests')
#
# tests = []
# for i in range(1, sheet.max_row):
#     tests.append(sheet.cell(row=i, column=3).value)
#
# tests = list(set(tests))
# print len(tests)
#
#
# book = xlwt.Workbook()
# sheet1 = book.add_sheet('sheet1')
#
# for i,e in enumerate(tests):
#     sheet1.write(i,1,e)
#
# name = "C:\Users\prath\Desktop\Capstone\srandom.xls"
# book.save(name)
# #book.save(TemporaryFile())