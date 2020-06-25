
##--------------------1.算术  运算符----------------------
a,b=10,21
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#取模
print(b%a)
#取整
print(b//a)
#  x**y   x的y次方
print(2**3)
# print(a/0)   0 作为除数会报错

#如果 参与运算的值中 有一个float，最后就会float
print(a*1.0)

#------------------------2.比较（关系）运算符-----------------
#  >  <  ==  >=  <==  !=    is(类似于===)
a,b=10,21
print(a>b)
print(a<b)
print(a==b)

#python中，判断可以连写
print(5<a<15)

#---------------------3.赋值 运算符------------------
# =  +=  -=  *=  /=  **=  //=  %=
d=10
d+=5  #相当于 d=d+5
print(d)
d**=2
print(d)
# i++  ++i  i--  --i  python没有


#-------------------4.逻辑运算符-------------
#  与and  或or  非not
print(  10>2 and 3>4  )
print(  True and False )

print(  True or False )
print( 4>3 )
print( not 4>3  )   #取反


#判断year 是不是闰年，是则是True，否则得Flase
#能被4整除 且不能被 100整除  或者  能被400整除
year=2020
print((year%4==0 and year%100!=0) or year%400==0)

#--------------------------5. 位  运算符---------------
# 把 10 进制 转为 2进制
a=60  #  111100
b=13  #  1101
#  &  按位与运算符：参与运算的两个值，如果两个相应位都为1，否则为0
print(a&b)
# |  按位或运算符，只要对应的二个二进制位有一个为1时，结果位就为1
print(a|b)

#--------------------6. 成员 运算符---------------------------
# in, not in
list2=[1,2,3]
print(4 in list2)
print(4 not in list2)

#---------------------7. 身份  运算符-------------------------------------
# 判断内存地址是否一样
#   is 是判断两个标识符是不是引用同一个对象
a=3
b=3
print(id(a))
print(id(b))
print(id(a)==id(b))
print(a is b)

#创建存储地址不一样的list
xiaoming=['苹果','橘子','西瓜']
hong=xiaoming
print(xiaoming is hong)
gang=['苹果','橘子','西瓜']
print(id(xiaoming))
print(id(gang))

hong[-1]='香蕉'
print(xiaoming)

xiaoli=xiaoming.copy()
xiaowang=xiaoming[:]
print(xiaoming is xiaoli)
print(xiaoming is xiaowang)




