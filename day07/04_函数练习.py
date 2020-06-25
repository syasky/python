#1、使用函数判断传入的对象长度是否大于5 ，是则返回 Yes，否返回No
def funcA(x):
    if len(x)>5:
        return 'Yes'
    else:
        return 'No'
print(funcA('2323'))
print(funcA([2,3,2,3]))
print(funcA({1,2,2,4}))
print(funcA(dict(a=1,b=2,c=3)))


#2、使用函数检查传入列表的长度，如果大于2，那么仅保留前两个长度 的内容，并将新内容返回给调用者。
def funcB(x:list):
    if len(x)>2:
        return x[0],x[1]
print(funcB([2,3,5,7]))

#3、比赛中我们在统计一些分数的时候经常斩头去尾一个分数，现在需要写一个函数，对传入的list进行斩头去尾。返回剩下的值。
# 提示  max(list) 返回；list 最大值  min(返回最小值)
def funcC(x:list):
    x.remove(max(x))
    x.remove(min(x))
    return x
print(funcC([12,25,23,26,2,2]))


#4、定义一个函数，输入不定个数的数字，使用循环计算，返回所有数字的和。
def funcD(*x):
    s=0
    for i in x:
         s=s+i
    return s
print(funcD(1,2,3,4,5))


#5、写个函数，通过遍历的方式计算任意 字符串的长度，并返回。
# def funcE(x:str):
#     a=len(x)
#     return a
# print(funcE('sajviousnlkvcnsoi'))

#遍历的写法
def getLen(str1):
    i = 0
    for each in str1:
        i+=1
    return  i

print(  getLen( 'abcd' ))


























