#定义有个类
class Person():
    #定义初始化函数
    def __init__(self,Name,Sex):
        self.name=Name
        self.sex=Sex

    def showInfo(self,city):
        print(f'我是{self.name},性别{self.sex},来自{city}')

xiaoming=Person('小明','男')
xiaohong=Person('小红','女')
#输出对象的属性
print(xiaoming.name)

# obj :object   对象   ，attr : attribute  属性
#------通过 getattr(obj,'attr')返回obj属性的值。找不到会报错
print(getattr(xiaoming,'name'))

#------通过 getattr(obj,'attr',default)返回obj属性的值。找不到会返回default
print(getattr(xiaoming,'job','杀手')) #返回小明的职业，如果没找到，就默认返回杀手

#--hasattr(obj,name)   返回 是否存在一个属性
print(hasattr(xiaoming,'job')) #False
print(hasattr(xiaohong,'sex')) #True

#--setattr(obj,'attr','value')  设置obj对象 的属性attr 是 value  （增加属性）
setattr(xiaoming,'job','学生')
setattr(xiaohong,'emotion','丰富')

print(xiaoming.job)
print(xiaohong.emotion)

#--delattr(obj,'attr') 删除obj对象的attr
delattr(xiaoming,'sex')
print(hasattr(xiaoming,'sex'))

#setattr(obj,'attr','value')   也有更改的作用
setattr(xiaohong,'sex','nan')
print(xiaohong.sex)













