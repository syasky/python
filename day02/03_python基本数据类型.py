
# None
a=None
print(a)
#判断数据类型用的函数是  type(a)
print(type(a))

#---------数字---------
print('---------数字---------')
b=2
print(type(b))
c=3.14
print(type(c))
#复数，虚部 默认为j，不能用其他的
d=5+2j
print(d)
print(type(d))

#---------布尔值---------
print('---------布尔值---------')
e=True
f=False
print(type(e))
#布尔值有多种表现形式
#我们可以用bool(xxx)判断，得到bool值
print(bool(123))   #True
print(bool(0))   #False
print(bool('O(n_n)O哈哈'))   #True
print(bool(''))   #空字符为False
print(bool(' '))   #空格为True
print(3>2)
g=200
print(g==200)  #判断 g 是否等于200，用两==

#   int()   float()
print(int(4.1))  # 4
print(float(5))   #5.0
print(int(True))  # 1
print(int(False))   #0
print(int(123))   #123
#print(int(abc1))不能转换，否则报错,除非是纯数字的字符串


#---------字符串---------
print('---------字符串---------')
str1='窝窝头'
print(str1)
print(type(str1))
print(type('一块钱四个'))
heihei='''
窝窝头，
一块钱四个，
嘿嘿
'''

print(type(heihei))
#str(xxx)把xxx转换成字符串
h=str(123)
print(h)
print(type(h))

#
print('aa'+'b')
print(1+2)
#print('a'+2) 会报错    + 左右 必须是 一样的数据类型


name='张三'
age=20
age=str(age)
print(name+','+'今年'+age+'岁')

name='张三'
age=20
print(name+','+'今年'+str(age)+'岁')

name='张三'
age=20
print(name,',今年',age,'岁',sep='')

#使用 变量  +  字符串进行拼接， 要 考虑到 数据类型一致
#  f'{变量}xxx' , 不需要考虑  数据类型

print(f'--{name},今年{age}岁')
#字符串  乘法
print('哈哈'*10)








