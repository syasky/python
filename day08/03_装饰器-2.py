
#  假设一个场景 。 你是饭店老板 . 你有三类员工 前台  服务员  厨师
#  每个人的工作不一样，用函数表示
#  饭店生意不行，原因是 没有问候，没有服务
# 整治 一下： 增加每个人的工作内容。不更改原来的

# 装饰器函数
#1.问好
def sayHello(func):
    def wrapper(*args,**kwargs):
        print('您好')
        func(*args,**kwargs)
    return wrapper

#2.倒水
def daoshui(func):
    def wrapper(*args,**kwargs):
        print('倒一杯卡布奇诺')
        func(*args,**kwargs)
    return wrapper

#3.说再见，欢迎再来
def sayBye(func):
    def wrapper(*args,**kwargs):
        func(*args, **kwargs)
        print('再见，欢迎再来')
    return wrapper


#---------------------
@sayHello
def qiantai():
    print('收银')
qiantai()

#
@sayHello
@daoshui
def fuwuyuan():
    print('上菜')
fuwuyuan()

#
@sayHello
@sayBye
def chuchi():
    print('做菜')
chuchi()




