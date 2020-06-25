
#闭包

def outer():
    a=10
    def inner():
        return a
    return inner
print(outer()())

#定义函数，用车音乐
def car():
    music='歌曲'
    def inner():
        return music
    return inner
print(car()())

#假设一个场景。大家 生产 榨汁机的。功耗，牌子
def Machine(paizi):
    gonghao = 2000
    def  zhazhiji(fruit):
        return  f'这是{paizi}的榨汁机，功耗{gonghao}W，可以做出{fruit}汁'
    return zhazhiji

jiuyang=Machine('九阳')
print(jiuyang('苹果'))
print(jiuyang('西瓜'))

#--------------------------------------------
#定义函数返回的x的y次方
def mypow(x,y):
    return x**y
print(mypow(2,3))
print(mypow(4,3))
#用闭包写，可以方便写其他函数
def anyPow(y):
    def inner(x):
        return x**y
    return inner

#平方函数
square=anyPow(2)
print(square(5))

#立方函数
cube=anyPow(3)
print(cube(5))














