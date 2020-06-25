
#class 声明一个类
class MyClass():
    name='python'
    #在类里面声明的函数，第一个参数，默认都是self，自带的，不用管他，必须得有
    def showinfo(self):
        print(f'{MyClass.name}语言正在发展')

#实例化对象
xx=MyClass()

#输出xx对象的属性
print(xx.name)
#调用它的方法
xx.showinfo()

def funcA():
    pass
funcA.t='ttt'
print(funcA.t)














