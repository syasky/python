#创建列表
list1=[1,2,3,'口罩','cov']
print(list1)
print(type(list1))
list2=[1,2,3,4]
print(list2)
list3=['a','b','c','d']
print(list3)

str1='hello'
list4=[str1,True,1,None,list3]
print(list4)

print('--------------------------------------------------------------')
'''
一个变量存三组数据
  1组：一万，二万，三万
  2组：四条，五条，六条
  3组：七筒，八筒，九筒
'''
mahjong = [
    ['一万','二万','三万'],
    ['四条','五条','六条'],
    ['七筒','八筒','九筒']
]
#mahjong 是一个二维列表
print(mahjong)

#三维数组
threeD=[mahjong,mahjong]
print(threeD)


print('===============操作===============')
#----------1.创建----------
#快速创建 单一 值 的 纯字符串组成的list,可以用 list(str)
list5=['a','b','c']
print(list5)
list6=list('abcdefg123')
print(list6)

#list()内直接放数字可以吗？
# list(123)   不可以，因为数字是不可迭代的，不能 list() 转换位列表

#创建不是单一数据的列表
#字符串 转换
#  str.split('x') 以x将str 进行分割成  list
list7='熊大/熊二/熊三'.split('/')
print(list7)

#----------2.读取列表----------
#使用 索引 或者 下标  从0开始代表第一个
list8=[2,3,4,'a','b','c']
#读取2
print(list8[0])
#读取'a'
print(list8[3])
#读取'c'.   读取可以反正读，最后一个是-1
print(list8[-1])

#假设 不知道 list8 多少个数，读取第10个数
#print（list8[9]） 会报错

#我们有个方法可以读取list 值的个数，或者说长度  len()   length
print(len(list8))

#--我们不仅可以读一个数据， 还可以读一堆数据
'''
语法：     list[start:end:step]
      start ：开始的位置，不写的话，默认开头为0
      end   ：接受的位置（不包含结束位），不屑的话，默认 结尾+1
      step  ： 读取的步长，默认是1，可以为负数倒着读
'''
list9=[1,2,3,4,5,6,7,8,9,10]
#list9=range(1,11)
#读取 list9 偶数位数据
print(list9[1:10:2])
print(list9[1:100:2])
print(list9[1::2])
#如果list的长度过长，恶魔也想往后取，但是数起来太麻烦，用len（）
print(list9[1:len(list9):2])

#rang list9 倒叙输出
print(list9[-1::-1])
# print(list9[10::-1])
print(list9[::-1])
print(list9[len(list9)::-1])

#读取8 6 4 2
print(list9[-3::-2])
print(list9[len(list9)-3::-2])

#正取2468，倒过来
print(list9[1:-2:2][::-1])

#读取数据，偶尔遇到一种情况，以xxx位置为基础，再操作
#如果读取某个数据往后的几个数据
#5往后的三个数据
print(list9.index(5))
print(list9[list9.index(5):list9.index(5)+3])
#字符串的 某个字符开始
str2='abcdefghij'
print(str2.find('d'))

#----------3.更新列表----------
print('----------3.更新列表----------')
list10=[10,20,30]
#增加数据到xxx的结尾
#语法：  xxx.append(yy)将yy增加到xxx列表的结尾
#增加40到结尾
list10.append(40)
print(list10)
#还可以增加任意数据类型
list10.append(['a','b','c'])
print(list10)

#xxx.insert(index,yy) 将yy放到xxx的index 索引位
list10.insert(0,1)
print(list10)
list10.insert(len(list10),'d')
print(list10)

#更改数据，xxx[index]='新值'
#如将1改为1024     当成将list10的某个索引位的值换个 内存地址 的指向
list10[0]=1024
print(list10)

#同一个值，内存地址一样
a=10
print(id(a))
b=10
print(id(b))
print(id(list10[1]))

ss=['a','b','c']
print(id(ss))
print(id(list10[5]))

ss1=['f','g']
list10.append(ss1)
print(list10)
print(id(ss1))
print(id(list10[-1]))
ss1[0]='ffffffffffff'
print(list10)

#----------4.删除数据----------
#语法  del xxx[索引]      .delete 单词
del list10[0]
print(list10)
# 也可以删除整个list10，释放内存
del list10
#删除后  操作list10  ，会报错
# print(list10)

#----------5.列表的操作符----------
#  +  连接列表
aa=[1,2,3]
bb=['4',5,6]
cc=aa+bb
print(cc)

# *  扩展 list的倍数个
shasha=aa*2
print(shasha)

# in   想象成去 教室找人，xx  in   更多结果 if 使用
classroom=['张三','李四','王五']
flag=('李四' in classroom)
print(flag)
print('李四' in classroom)

flag2=('沙沙' in classroom)
print(flag2)
#if
if '张三' in classroom:
    print('请你吃饭')




