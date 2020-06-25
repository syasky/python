#xlrd 我们已经安装过了
import xlrd
# 打开本地文件
workbook=xlrd.open_workbook('某公司贸易数据.xlsx')

# 2. 获取工作表
#获取工作表 组成的list
sheets=workbook.sheets()
print(sheets)

#3. 获取具体的数据表
#3.1 使用下标获取
#如：第一张表
#sheetOne=sheet[0]

#3.2使用workbook的函数获取
# sheetOne=workbook.sheet_by_index(0)
# print(sheetOne)

#3.3获取所有表的名称：str 组成的list
sheetNames=workbook.sheet_names()
# print(sheetName)
sheetOne=workbook.sheet_by_name(sheetNames[0])
# print(sheetOne)

#4.获取  工作表的  行数  与  列数
row=sheetOne.nrows
column=sheetOne.ncols
print(f'几行：{row},  几列：{column}')

#  行：row  列：column
#5. 行与列的读取
#读取行：   sheetOne.row_values(index) 返回index行的值组成的 list
#读取列：   sheetOne.clo_values(index) 返回index列的值组成的 list
#如：读取第二行和列
print(sheetOne.row_values(1))
print(sheetOne.col_values(1))

#输出所有行
x=sheetOne.nrows
for i in range(x):
    print(sheetOne.row_values(i))

#6.精确到单元格的值

#思路1：精确到某行或某列，然后使用下标
#如：输出  寿司
print(sheetOne.row_values(4)[-1])

#思路2：sheetObj,cell(行数，列数) 返回 单元格 对象
# sheetObj,cell(行数，列数).value  就是值
print(sheetOne.cell(4,2).value)

#思路3： sheetObj.cell_value(行数，列数) 直接返回单元格的值
print(sheetOne.cell_value(4,2))

#使用循环嵌套，输出所有  单元格的值:
a=sheetOne.nrows
b=sheetOne.ncols
for x in range(a):
    for y in range(b):
        print(sheetOne.cell_value(x,y))




