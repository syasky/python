#动物类
class Animal():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self,food):
        print(f'我是{self.name},爱吃{food}')

#创建  Dog  类   继承  Animal 类
class Dog(Animal):
    #从  Animal 类继承属性,覆盖
    def __init__(self,name,age):
        super().__init__(name,age)

# 创建  Cat  类   继承  Animal 类
class Cat(Animal):
    # 从  Animal 类继承属性
    pass

#实例化对象
husky=Dog('哈士奇',2)
print(husky.name)
print(husky.age)
husky.eat('肉')

daju=Cat('大橘',3)
print(daju.name)
print(daju.age)
daju.eat('鱼')







