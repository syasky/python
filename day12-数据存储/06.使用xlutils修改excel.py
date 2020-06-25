
#需要安装 xlutils 模块
import xlrd
from xlutils.copy import copy
#读取一个工作簿
wb=xlrd.open_workbook('newOne.xls')
#复制一份
copyed=copy(wb)
#读取第一份
sheetOne=copyed.get_sheet(0)
#写入
sheetOne.write(0,0,'我是覆盖后的数据')
sheetOne.write(0,5,'666')
#保存，如果原文件名相同，就是覆盖了。不同就是新存一个文件
copyed.save('newOne.xls')