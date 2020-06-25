#tuple   不可更改的数据类型

#语法   xxx=(1,2,3)
tuple1=(1,2,3)
print(tuple1)
#而且可以省略括号
tuple2=4,5,6
print(tuple2)

#注意：   单元素的元组创建时要注意,加一个逗号
tuple3=('aa',)
print(type(tuple3))
tuple4='bb',
print(type(tuple4))

#元组可以放多种数据
tuple5=('a',1,True,None,[1,2,3],tuple4)
print(tuple5)

#元组可以多变量一次赋值
a,b,c=100,200,300
print(a)
print(b)
print(c)
d,e=[400,500]
print(d)
print(e)
f,g=([5,6],[7,8])
print(f)
#题目：将两个变量互换值
num1=1000
num2=2000
print(num1,num2)
num2,num1=num1,num2
print(num1,num2)

#tuple()  可以将一些变量转为元组
print(tuple('abc'))
print(tuple([2,3,4]))

#------更新数据-----
#因为元组不能修改，所以，不能增加，不能修改，不能删除   某个值

#-----------只能查询元组----------
#  与  列表  一模一样

#元组的操作符 与 list 一样一样的的。 + * in



