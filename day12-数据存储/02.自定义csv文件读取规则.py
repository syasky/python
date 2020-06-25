import csv
'''
注册新的读取规则:语法
csv.register_dialect('规则名称',delimiter='分隔符')
注销 规则
csv.unregister_dialect('规则名称':str)
'''
csv.register_dialect('mydialect',delimiter='|')
with open('newcsv.csv','r',encoding='utf-8') as file:
    csvfile=csv.reader(file,dialect='mydialect')

    for each_line in csvfile:
        print(each_line)





