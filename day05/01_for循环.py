'''
for  xxx  in  yyyy:
     dosthong
'''

#1.输出 一个 字符串中的每一个 字母
for each in 'hello':
    print(each)
    # print(1)

#认识一下  range(start,end,step)    end 不包含
#range(1,7,2)  你就当成[1,3,5]去使用
#2.输出 1-20内的奇数
for item in range(1,20,2):
    print(item)
print(list(range(1,20,2)))

#3.输出1-100内3的整数倍，在同一行输出
print(list(range(3,100,3)))

for i in range(1,100):
    if i%3==0:
        print(i,end=' ')
print()
for i in range(3,100,3):
    print(i,end=' ')
print()
for i in range(1,34):
    print(3*i,end=' ')
print()
#4. 使用while 或 for 循环 将[12,25,35,40,88,87]奇偶分开
list2=[12,25,35,40,88,87]
# index=0
# while index<len(list2):
#     print(list2[index])
#     index+=1
#使用for
# for each in list2:
#     print(each)

odd=[]
even=[]
for each in list2:
    if each%2==0:even.append(each)
    if each%2==1:odd.append(each)
print(odd)
print(even)

#5. 已知某小组 学号是1-4['张三','李四','王五','赵六']
#需要for 输出这个格式：1号->张三
team=['张三','李四','王五','赵六']
# a=0
# for each in team:
#     a+=1
#     print(a,'号->',each)

for i in range(0,len(team)):
    print(f'{i+1}号->{team[i]}')

num=[1,2,3,4]
for i in range(0,4):
    print(f'{num[i]}号->{team[i]}')

#6 使用 for 遍历 字典
dict1=dict(a=1,b=22,c=333,d=4444)
print(dict1)
#输出字典的每一个key
for i in dict1:
    print(i)     #每个  i 是key

#输出值
for i in dict1:
    print(dict1[i])

#对于 字典，有两个函数
#dict1.keys() 所有key组成的 可迭代对象
#dict1.values() 所有value组成的 可迭代对象
print(dict1.keys())
print(dict1.values())
for i in dict1.keys():
    print(i)
for i in dict1.values():
    print(i)

'''
就两种玩法
for each in 可迭代对象：
     xxx
     
for i om range(0,n):
    yyy
'''

#7. 小明同学迟到 罚跑5圈，打印记录
for i in range(5):
    print(f'小明同学跑了{i+1}圈了。')




