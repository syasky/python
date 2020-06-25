
#目的：已又一个list2=list(range(0,20))
# list2=list(range(0,21))
# print(list2)

list2=[17,0,2,3,6,7,9,10,1,11,12,5,13,4,14,15,16,18,8,19]

#1.取出list2中的奇数，得到一个list
#新建list，使用append()方法
odd=[]
for each in list2:
    if each%2==1:
        odd.append(each)
print(odd)

#2.推导式写法
'''
yy=[对each的各种操作后的值 for each in xxx （if zzz）]
'''
odd2=[each for each in list2 if each%2==1]
print(odd2)

###带有逻辑的推导式
#创建一个list3，它是1-10的2倍+3
list3=[each*2+3 for each in range(1,11)]
print(list3)

#取出list2中的数据为奇数的，且返回这些数的2倍加1
list4=[each*2+1 for each in [each2 for each2 in list2 if each2%2==1]]
print(list4)

#创建一个 1-10的平方数列表
list5=[each*each for each in range(1,11)]
print(list5)

#
list2=[17,0,2,3,6,7,9,10,1,11,12,5,13,4,14,15,16,18,8,19]
#得到list2中，即使3的倍数，又小于15的数 的平方根 保留2位小数的list
list6=[float('%.2f'%each**0.5) for each in list2 if each%3==0 and each<15]
print(list6)


#1.list2是list1的两倍
list1=[1,3,5,7,9]
list2=[each*2 for each in list1]
print(list2)
#2.list3是list2中的所有数字
list2=[1,2,3,4,'d','a','b','c',5,6]
list3=[each for each in list2 if type(each)==int]
print(list3)
# 3.list3是list2中的所有偶数
list2=[1,2,3,4,'d','a','b','c',5,6]
list3=[each for each in list2 if type(each)==int and each%2==0]
print(list3)

#如果有浮点
list2=[1,2,3,4,'d','a','b','c',5,6.0,2.5]
list4=[each for each in list2 if type(each) in [int,float]]
print(list4)

