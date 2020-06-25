
class A(object):
    def __init__(self,name):
        self.name=name

class B(object):
    def __init__(self,age):
        self.age=age

class C(A,B):
    def __init__(self,name,age):
        A.__init__(self,name)
        B.__init__(self,age)

xiaoc=C('jack',20)
print(xiaoc.name)
print(xiaoc.age)

print('--------------------------------------------------')
#创建生物类
class Biology(object):
    def __init__(self,name):
        self.name=name

#创建动物类
class Animal(Biology):
    def __init__(self,name,Atype):
        super().__init__(name)
        self.type=Atype
    def showLiveTime(self,n=20):
        print(f'一般可以活{n}年')
#猫类
class Cat(Animal):
    def __init__(self,name,Atype,color):
        super().__init__(name,Atype)
        self.color=color

    def showLiveTime(self,n=15):
        print(f'一般可以活{n}年')

#实例化对象
ragdoll=Cat('布偶猫','猫科','白色')
print(ragdoll.name)

#调用方法1
ragdoll.showLiveTime()   #如果类里有这个函数，就使用本函数，没有则使用继承的类里面的函数

# 调用 : 方法 2  ，由 不同类发起 ,可以指定哪个类中的函数运行
Cat.showLiveTime(ragdoll)
Animal.showLiveTime(ragdoll)

