
def mypow(x,y):
    return x**y

class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

Year=2020

# print(mypow(10,3))
#运行函数的时候，如果作为 模块被导入
#有运行的话， 都  要判断

#判断是否在本文件
if __name__=='__main__':
    print(mypow(10,3))




