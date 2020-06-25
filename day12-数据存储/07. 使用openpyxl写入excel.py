#Workbook 的 W 是要大写的
from openpyxl import Workbook

#1.实例化对象，创建工作簿
wb=Workbook()

#2.获取第一张表，wb.active 默认第一张
sheet=wb.active

#3.给表取个名称，其实就是属性赋值
sheet.title='表d名称 1'

#4.写入数据，按行写入的 sheet.append( list类型的数据)
sheet.append([1,2,3])

#5.保存
wb.save('new2.xlsx')





