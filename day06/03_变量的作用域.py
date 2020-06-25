'''
# 全局变量
s=100

def funcA():
    # 局部变量
    a=1
    print(a)
    print(s)
funcA()

# print(a) 报错
'''


s=100
def funcB():
    a=2
    print(a)
    s=300
    print(s)

funcB()
print(s)
print('----------------------------')
'''
s = 200
def funcB():
    a = 2
    print(a)
    # print(s)  不能先使用再声明
    s = 300
    print(s)

funcB()
print(s)
'''

# 可以局部改全局
s3=10
def funcC():
    # 借助  global  可以在局部使用 并 更改全局变量
    global s3
    s3+=20
    print(s3)
funcC()
print(s3)

# 有时候发现 不用global 也能更改全局变量的值
list2=[1,2,3]
def funcD(x):
    print(x)
    x[0]=100
    print(x)
funcD(list2)
print(list2)








