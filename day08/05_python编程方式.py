
#1.面向过程
#从上往下，根据业务逻辑写代码
# 如 if-else  或者上下有逻辑关系的语句
#判断年份是否是闰年
year=2020
if year%4==0 and year%100!=0 or year%400==0:
    print(f'{year}是闰年')
else:
    print(f'{year}不是闰年')


#2. 函数式编程
def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f'{year}是闰年')
    else:
        print(f'{year}不是闰年')
isLeapYear(2020)



