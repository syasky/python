import math
import random

#1--   random.chioce( seq ) 从seq中取一个随机对象
print(random.choice(range(10)))
print(random.choice(['a','c','张三','list']))

#从1-100中随机取一个5的倍数
num1=random.choice(range(5,101,5))
print(num1)
# print(random.randrange(5,101,5))

#语法：
#2--   random.randrange([start,] stop [,step]) 从指定start-stop的步长为step数据中取一个随机整数。 start和step可有可无
print(random.randrange(5,101,5))

#取一个1-50的随机整数
print(random.randrange(1,50))

#3--   random.random()  取一个0-1的随机小数
print(random.random())
#0-1的数乘以50  0-50的数 再向上取整
print(math.ceil(random.random()*50))

#4--   shuffle(list) 将 list 随机排序，直接操作在原数据上的，不会返回新对象
list2=list('abc12345')
print(list2)
random.shuffle(list2)
print(list2)

#5-- 随机实数  random.uniform(x,y)   返回x-y的随机实数
print(random.uniform(-2,2))