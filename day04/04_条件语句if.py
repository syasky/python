
'''
缩进：4个空格
语法：
if 条件：
      dosthing
elif 条件：
      dosthing
elif 条件：
      dosthing
else：
      dosthing
'''

# 判断闰年
year=2020
if year%4==0 and year%100!=0 or year%400==0:
    print(f'{year}是闰年')

#输入 三个数，判断能否组成一个三角形
a=int(input('输入第1个数：'))
b=int(input('输入第2个数：'))
c=int(input('输入第3个数：'))
if a+b>c and a+c>b and b+c>a:
    print('能组成三角形')
else:
    print('不能组成三角形')

#判断三边能否组成直角三角形
a=int(input('输入第1个数：'))
b=int(input('输入第2个数：'))
c=int(input('输入第3个数：'))
if a+b>c and a+c>b and b+c>a:
    if a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
        print('能组成直角三角形')
    else:
        print('不能组成直角三角形')
# 判断三边能否组成直角三角形,随便找出斜边
a=int(input('输入第1个数：'))
b=int(input('输入第2个数：'))
c=int(input('输入第3个数：'))
if a+b>c and a+c>b and b+c>a:
    if a*a+b*b==c*c:
        print(f'斜边是{c}')
    if b*b+c*c==a*a:
        print(f'斜边是{a}')
    if  a*a+c*c==b*b:
        print(f'斜边是{b}')

# max(a,b,c)返回最大值
print(max(10,8,6))















