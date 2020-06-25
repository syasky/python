#定义有个类
class Person():
    #定义初始化函数
    def __init__(self,Name,Sex):
        self.name=Name
        self.sex=Sex

    def showInfo(self,city):
        print(f'我是{self.name},性别{self.sex},来自{city}')

gebilaowang=Person('隔壁老王','男')
print(gebilaowang.name)
print(gebilaowang.sex)
gebilaowang.showInfo('隔壁')


#创建一个dog类，规定有名字有颜色，有四条腿，会叫并且说自己有几条腿
class dog():
    def __init__(self,name,colour,leg,call):
        self.name = name
        self.colour = colour
        self.leg=leg
        self.call=call

    def showInfo(self):
        print(f'{self.call},我是{self.name},颜色{self.colour},有四条{self.leg}')
xiaogou=dog('小黑','绿色','腿','汪汪汪')
print(xiaogou.name)
print(xiaogou.colour)
xiaogou.showInfo()




