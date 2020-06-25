
#return 作用


# 1. 结束函数
#假设一张纸 0.08毫米。对着第三次超越珠穆朗玛峰 8848.13米
def funcA():
    h=0.08/1000
    count=0
    for i in range(1,100):
        h*=2
        if h>8848.13:
            print(i)
            return
funcA()

def funcB():
    print(1)
    print(2)
    return
    print(3)
    print(4)
funcB()


##--2,返回一个结果
a=2
print(id(a))
print(type(a))
print(float(a))
print(funcA())

#2.1 返回的值都一样
def playGame(game):
    print(game,'进行中。。。')
    return 'Game Over'

result1=playGame('跳一跳')
result2=playGame('连连看')
result3=playGame('闪击快打')
print(result1)
print(result2)
print(result3)

#自己定义一个函数，用来处理 出入的数据，进行求和，最后返回和
def mysum(x:list):
    s=0
    for each in x:
        s+=each
    return s
print(mysum([1,2,3,4,5]))
print(mysum(range(11)))
#系统自带求和函数sum()
print(sum(range(11)))

##练习一： 定义函数，返回传入的纯数字的list  的平方和
#写法一：
def cxk(list1):
    s=0
    for each in list1:
        s+=each**2
    return s
print(cxk([2,3,4]))

#写法二： 用推导式快速生成  平方数 list  然后返回和
def cxk(list2):
    slist=[x**2 for x in list2]
    he=sum(slist)
    return he
print(cxk([2,3,4]))

#精简版
def sumlist(list3):
    return sum([each**2 for each in list3])
print(sumlist([2, 3, 4]))





