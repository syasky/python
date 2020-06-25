import math

# abs(x) 返回x的绝对值
print(abs(-10))

#math.ceil(x) 向上取整，也就是 进1法
print(math.ceil(3.4))

#math.floor(x) 向下取整
print(math.floor(3.4))

# round(number,ndigits=n)  对number 保留n位小数，四舍五入
print(round(5.3))
print(round(5.3,1))
print(round(3.141592,2))
print(round(math.pi,3))

#比较大小
#导入 操作符 模块
import operator
a,b=20,10
print(a>b)
print(operator.gt(a,b))
print(operator.lt(a,b))
print(operator.eq(a,b))
#大于等于
print(operator.ge(a,b))

#操作符 + 的替代品
print('e' in 'abcde')
print(operator.contains('abcde','e'))

#fabs()
print(math.fabs(-30))  #30.0

# math.exp(n) 返回自然数常量e的n次方
print( math. exp(2))
# log(x)求对数。 默认以自然数常量e为底。 log(值， 底)
print(math.log(16,4) )
print(math.log(math.exp(3)) )

#math.log10(x) 以10位底求 对数
print(math.log10(10000))

#max(x1,x2....)返回最大值
#min(x1,x2....)返回最小值
print(max(1,3,5,9,8))
print(min([1,3,5,8,4,6]))

#math.modf(x) 返回x的小数部分与整数部分
print(math.modf(3.141))

#pow(x,y)  相当于 x**y
print( pow(3,3))
print(4**0.5)   #平方根
print(pow(4,1/3))  #三次方根 （立方根）

#  math.sqrt(x)   返回 x 的平方根
#返回4的平方根
print(math.sqrt(4))
print(4**0.5)   #平方根


#练习： 使用推导式，快速创建一个 1-20内的  偶数的  平方根保留3位小数后  组成的  列表
# for i in range(1,21):
#     if(i%2==0):
#         a=i**0.5
#         print(round(a,3))
list1=[round(math.sqrt(each),3) for each in range(2,21,2)]
print(list1)

#自然数常量
print(math.e)

#阶乘
print(math.factorial(4))

