#-----1 必备参数
#-----2 关键字参数    见前一天的代码

#-----3 默认参数，（缺省参数）,在定义的时候已经给了一个值
#统计  身份信息，有年龄
def showInfo(name,age=18):
    print(f'{name},今年{age}岁.')
#调用函数
showInfo('小明',20)
showInfo('小红')
#我们一直在使用的print 就有很多的默认参数
# 打一个print，按住ctrl 左击它，查看文档       # sep就可以更改默认参数
print(10,20,30,sep=' ')
print(2020,4,2,sep='/')

#-！！！-4 不定长参数

def funcD(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)   #使用的时候不用*号
    print(kwargs)  #使用的时候不用*号

#调用
funcD('熊大',10)
#  args：以元组的形式手机多余的普通参数 ，
#  kwargs：以 字典的形式收集多余的 key = value 参数
funcD('范闲',20,'朵朵',['熊大','熊二'],sex='男',book=['庆余年','熊出没'])
















