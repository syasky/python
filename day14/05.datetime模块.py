import time
from datetime import  datetime

# 获取当前时间对象
nowtime = datetime.today()
print(nowtime)

# 创建 指定如期的 时间对象
spe_time = datetime(2020,5,20,18,0,0)
print(spe_time)

# 将字符串转为时间对象
timestr = '2020/04/01 12:00:00'
timestr_obj = datetime.strptime(timestr,'%Y/%m/%d %H:%M:%S' )
print(timestr_obj)
print(type(timestr_obj))

# 将时间戳变成 datetime 对象
print( datetime.fromtimestamp( time.time() ) )

#  datetime 对象可以通过属性获取 年月日时分秒等数值
print(nowtime.year )
print(nowtime.month )
print(nowtime.day )
print(nowtime.hour )
print(nowtime.minute )
print(nowtime.second )
print(nowtime.microsecond )

# 很多时候，我们将年月日一起说， 时分秒一起说
print( nowtime.date() )

print(nowtime.time())

# 获取今天是周几
print(  nowtime.weekday() )  # 从 0开始算周一
print( nowtime.isoweekday() )  # 从 1 开始算周一

# 对象变字符串
# datetime.strftime()
print( nowtime.strftime('time: %Y-%m-%d') )