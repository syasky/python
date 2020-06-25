
#导入模块
import csv

# with open('2.csv','w',encoding='utf-8') as file:
#     #转为csv的 写入对象
#     csvfile=csv.writer(file)
#     #写入一行
#     csvfile.writerow(['序号','网址','名称'])
#     #写入多行
#     #先准备一个二位列表
#     data = [
#         [1, 'http://www.baidu.com', '百度'],
#         [2, 'http://www.jd.com', '京东'],
#         [3, 'http://www.taobao.com', '淘宝']
#     ]
#     #
#     csvfile.writerows(data)

#解决空行问题，方法一
# with open('2.csv','w',encoding='utf-8',newline='') as file:
#     #转为csv的 写入对象
#     csvfile=csv.writer(file)
#     #写入一行
#     csvfile.writerow(['序号','网址','名称'])
#     #写入多行
#     #先准备一个二位列表
#     data = [
#         [1, 'http://www.baidu.com', '百度'],
#         [2, 'http://www.jd.com', '京东'],
#         [3, 'http://www.taobao.com', '淘宝']
#     ]
#     #
#     csvfile.writerows(data)
#如果报错 PermissionError  ，就是权限问题，文件被占用，关闭打开文件的软件即可


#解决空行问题，方法二
#使用其他模块  codecs
import codecs
with open('2.csv','w',encoding='utf-8',newline='') as file:
    #转为csv的 写入对象
    csvfile=csv.writer(file)
    #写入一行
    csvfile.writerow(['序号','网址','名称'])
    #写入多行
    #先准备一个二位列表
    data = [
        [1, 'http://www.baidu.com', '百度'],
        [2, 'http://www.jd.com', '京东'],
        [3, 'http://www.taobao.com', '淘宝']
    ]
    #
    csvfile.writerows(data)





