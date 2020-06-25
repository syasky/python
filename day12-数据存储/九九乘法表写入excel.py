#从第二行第一列开始  写入一个九九乘法表进入excel
import xlwt
workbook=xlwt.Workbook()
sheet=workbook.add_sheet('newSheet')

for i in range(1,10):
    for j in range(1,i+1):
        a=i*j
        sheet.write(i, j-1, f'{j}*{i}={a}')

workbook.save('99.xls')