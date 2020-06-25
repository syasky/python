# 不可更改的数据类型
str1='abc'
num1=123
tuple1=1,2,3

#可更改的
list1=[1,2,3]
list1[0]=10
dict1={'a':3,'b':4}
dict1['b']=40

def funcA(x):
    x[-1]=1000
funcA(list1)
print(list1)

# 如果传 不可更改的数据
# funcA(str1)  会报错

# 可以在定义的时候顺便知名一下 参数的类型，传值的时候会方便不少
#def xxx(a:int,b:str,c:list)

# 定义一个函数，返回 这个 年份 是不是 闰年
def  isrun(year:int):
    if year%4==0 and year%100!=0 or year%400==0:
        return f'{year}是闰年'
    else:
        return f'{year}不是闰年'
result1=isrun(2020)
print(result1)
print(isrun(2020))

print('-------------------------------------------------')
# 值传递，传入的是 不可变的时候就是值传递
a=10
b=[2,3,4]
def funcB(x):
    print(x)
    x=100
    print(x)
funcB(a)
print(a)

a=10
b=[2,3,4]
def funcB(x):
    print(x)
    x=100
    print(x)
funcB(b)
print(b)

a=10
b=[2,3,4]
def funcB(x):
    print(x)
    x[0]=100
    print(x)
funcB(b)
print(b)















