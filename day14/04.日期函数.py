
#导入模块
import time

#获得时间戳
print(time.time())

#获得时间元组
localtime=time.localtime()
print(localtime)

#格式化时间对象
#自带的函数
print(time.asctime())

#自定义格式化时间  str format time
print(time.strftime('%Y %m %d %H:%M:%S',localtime))

#其他符号
print(time.strftime('%Y %m %d %H:%M:%S %A %a %B %b %j %U %W'),localtime)


#日历
import calendar
cal=calendar.month(2020,5)
print(cal)


#常用函数
#将时间元组变回时间戳
print(time.mktime(localtime))

#判断是不是闰年
print(calendar.isleap(2020))
# 返回 year1 -year2 间的闰年数量
print( calendar.leapdays(2000,2019))


