
#1.增加   记录函数的执行时间 的功能
import time
# print(time.time())   1970-1-1 00:00:00 到现在过了多少秒
# time.sleep(2)        程序睡眠几秒

#1.1原始函数  生成一个 1-100 平方数的列表
def funcA():
    time.sleep(1)
    list1=[]
    for i in range(1,100):
        list1.append(i**2)
        #也可以直接用推导式  list2=[i**2 for i in range(1,100)]
    return list1

#1.2增加  打印执行函数
#--1.2.1 :在原始函数内修改
def funcB():
    #获取开始时间
    start=time.time()
    time.sleep(1)    #给程序运行多加一秒
    list1=[]
    for i in range(1,100):
        list1.append(i**2)
        #也可以直接用推导式  list2=[i**2 for i in range(1,100)]
    end=time.time()
    print(f'{funcB.__name__}的执行时间为：{end-start}')
    return list1
print(funcB())
#如果是在公司，有好几个人需要对 函数功能进行增加。就会有麻烦
#1.函数原始结构被修改，花时间
#2.张三改，李四改。每个人内容乱了

# 1.2.2 进阶版。新建一个函数，在函数内执行已经存在的函数，不修改原始函数的结构
#虽然有记录时间的效果，但是是间接的实现这功能
def funcC():
    start=time.time()
    #执行已与有函数
    result=funcA()
    end=time.time()
    print(f'{funcC.__name__}的执行时间为：{end-start}')
    return result
print(funcC())
#缺点  需要对大量的 函数 增加功能时，写起来要很多个

#1.2.3 进阶版  进化，建一个函数，在函数内执行已经存在的函数，以参数的形式
def funcD(funcName):
    start = time.time()
    # 执行已与有函数
    result = funcName()
    end = time.time()
    print(f'{funcD.__name__}的执行时间为：{end - start}')
    return result
#只需要将funcA 当成参数传入即可灵活 打印执行时间，但是也是间接的
print(funcD(funcA))

print('-------------------------------------------------------------------------------')
#1.2.3  装饰器
#定义装饰器函数
def deco(funcName):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=funcName(*args,**kwargs)
        end=time.time()
        print(f'装饰器函数记录-程序执行时间为{end-start}')
        return result
    return wrapper

#如何使用装饰器函数，就像你在聊天@xxx一样A
@deco
def funcAA():
    time.sleep(1)
    list1=[]
    for i in range(1,100):
        list1.append(i**2)
        #也可以直接用推导式  list2=[i**2 for i in range(1,100)]
    return list1
print(funcAA())


@deco
def fun(x):
    time.sleep(2)
    print(x)
fun(123)