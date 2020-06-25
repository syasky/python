
class Person():
    __doc__ = '文档字符串'
    name='生产者'
    #类的内部  用__两个下划线开头的属性，只能在内部使用 self._使用，外部部门使用
    __secret='我是内部的私有属性'

    def showInfo(self):
        print(f'可以在内部使用 私有变量：{self.__secret}')
        self.__private()
    #定义私有函数
    def __private(self):
        print(f'我是私有方法')


print(Person.__doc__)
print(Person.__name__)
print(type(Person.__name__))
print(Person.name)
print(Person.__module__)
print(Person.__dict__)

# print(Person.__secret)  #会报错  （私有属性在外部不可用）

#由类发起的函数调用，该有参数还得有，不然报错
# Person.showInfo()

hanbing=Person()
hanbing.showInfo()
Person.showInfo(hanbing)

#hanbing.__private()  #会报错,私有方法只能在类内部使用


#定义学生类，属性：姓名，年龄，三门成绩
#类：输出姓名；输出年龄；输出三门中最高的成绩
class students():
    def __init__(self,name:str,age:int,achievement:list):
        self.name=name
        self.age=age
        self.achievement=achievement
    def get_name(self):
        print(f'姓名是{self.name}')
    def get_age(self):
        print(f'年龄是{self.age}')
    def get_course(self):
        print(f'最好的成绩是{max(self.achievement)}')

laowang=students('老王',20,[60,90,79])
laowang.get_name()
laowang.get_age()
laowang.get_course()







