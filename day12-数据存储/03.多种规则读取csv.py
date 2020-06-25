import csv
'''
注册新的读取规则:语法
csv.register_dialect('规则名称',delimiter='分隔符')
注销 规则
csv.unregister_dialect('规则名称':str)
'''
csv.register_dialect('mydialect',delimiter='|')

with open('newcsv.csv','r',encoding='utf-8') as file:
    csvfile=csv.reader(file)

    for i,each_line in enumerate(csvfile):
        print(i,each_line)
        #判断  终止for循环。file对象就读了一部分
        if i>=2:
            break
    #使用  其他规则读继续取file对象
    csvfile2=csv.reader(file,dialect='mydialect')
    for each in csvfile2:
        print(each)





