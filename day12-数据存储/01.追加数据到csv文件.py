
import csv

#参数 mode='a'  决定增加内容，不会有删减
with open('newcsv.csv',mode='a',encoding='utf-8',newline='') as file:
    #转为csv文件对象
    csvfile=csv.writer(file)
    #使用csv对象的方法去写入数据
    # data=[
    #     [1, 'http://www.baidu.com', '百度'],
    #     [2, 'http://www.jd.com', '京东'],
    #     [3, 'http://www.taobao.com', '淘宝']
    # ]
    # csvfile.writerows(data)

    #追加特殊数据进去
    csvfile.writerow(['江苏省|扬州市|市区'])
    csvfile.writerow(['江苏省|镇江市|郊区'])
    csvfile.writerow(['江苏省|苏州市|县城'])

