
import csv

with open('2.csv','r',encoding='utf-8') as file:
    #转为 csv读取对象
    csvfile=csv.reader(file)
    #csvfile , 是一个可迭代对象，只能使用一次

    #可以用for去迭代
    for each in csvfile:
        print(each)

    #也可以用list转换
    data=list(csvfile)
    print(data)

#for和list只能使用一次，因为第一次会读完










