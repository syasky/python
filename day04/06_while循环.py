# while 循环:
'''
while 条件:
    dosthing
'''

#使用if判断num<5 并输出num,每次num+=1
# num=1
# while(num<5):
#     print(num)
#     num += 1

# demo1:     a=1,用while 输出20以内的奇数
a=1
while(a<=20):
    if a%2!=0:
        print(a)
    a+=1

#demo2:    输出100内3的倍数
b=1
while b<100:
    if b%3==0:
        print(b,end=' ')
    b+=1

b=3
while b<100:
    print(b,end=' ')
    b+=3

b=1
while 3*b<100:
    print(3*b,end=' ')
    b+=1


#----------------------------
#while---else---
c=1
while c<4:
    print(c)
    c+=1
else:
    print('循环结束后执行else结构体')





