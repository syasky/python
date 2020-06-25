
#定义一个函数，返回两个数字参数的和
def funcA(a,b):
    return a+b

print(funcA(10,20))

#匿名函数的语法： lambda  arg1,arg2,... :表达式
#匿名函数的形式：整体思想
print((lambda a,b:a+b)(20,30))

#匿名函数也可以用变量来接受
funcB=(lambda a,b:a+b)
print(funcB(30,40))

#无参数  匿名函数    ，game over
g=lambda:'Game Over'
print(g())

#返回某个数的平方
square =lambda x:x**2
print(square(10))


##------函数中返回函数-------
def funcB(x):
    return lambda y:x+y

resl=funcB(11)  #或者  resl=lambda y:11+y
print(resl)
print(resl(22))

print(funcB(22)(33))

#def 内 再用def
def funcC(x):
    def funcD(y):
        return x+y
    return funcD
print(funcC(25)(15))



#lambda后用 lambda
aa=lambda x:lambda y:x+y
print(aa(12)(22))









