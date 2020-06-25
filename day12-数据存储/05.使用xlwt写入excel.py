#导入模块
import xlwt

#1.创建工作簿对象
workbook=xlwt.Workbook()

#2.创建工作表对象，并且命名
sheet=workbook.add_sheet('newSheet')

#3.写入数据的语法：sheet.write(row,col,value) 第cow行col列写入value值
#第一行第一列写入0
sheet.write(0,0,0)
sheet.write(0,1,'1')
sheet.write(0,2,'哈哈')

# #4.保存：工作簿对象.save('fileName')
workbook.save('newOne.xls')



#从第二行第一列开始  写入一个九九乘法表进入excel
#见 九九乘法表写入excel  文件

