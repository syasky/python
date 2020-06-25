#print

#print(数据)
print(123)

#多数据，一次输出
name='xiongda'
age=10
print(name,'今年',age,'岁')
#sep=''  参数指定print 多个值之间用上面连接
print(name,'今年',age,'岁',sep='--')

#配合  格式化字符串  digit
# str1='%s is %d years old'%(name,age)
# print(str1)
# print('%s is %s years old'%('xionger',6))

#print('%s is %d years old'%('xiongxiao','2'))  占位符要数据类型对象，%s 可特殊

'''
    %s   是一个字符串占位符
    %10s  是一个字符串占位符，占10个字符位，默认靠  右  显示。
    %-10s  是一个字符串占位符，占10个字符位，默认靠  左  显示。
'''
#可以用来美观的展示数据
print('姓名:%s,性别:%s,年龄:%s'%('xiongda','男',10))
print('姓名:%s,性别:%s,年龄:%s'%('xiyangyang','男',6))
print('姓名:%s,性别:%s,年龄:%s'%('huitailang','男',3))

#通过占位符+数字
print('姓名:%15s,性别:%s,年龄:%2s'%('xiongda','男',10))
print('姓名:%15s,性别:%s,年龄:%2s'%('xiyangyang','男',6))
print('姓名:%15s,性别:%s,年龄:%2s'%('huitailang','男',3))

print('姓名:%-15s,性别:%s,年龄:%-2s'%('xiongda','男',10))
print('姓名:%-15s,性别:%s,年龄:%-2s'%('xiyangyang','男',6))
print('姓名:%-15s,性别:%s,年龄:%-2s'%('huitailang','男',3))


#重要的知识点，用来将字符串 与 变量 连起来输出
value='张三'
age=20
num=666.66
#将上面三个变量 用  姓名：  ，年龄：  ，爱好： 。输出
#方法1： 占位符%s  %d  %f
#方法2：str.format(value1,value2,value3,......)
str2='姓名:{},年龄:{},爱好:{}'.format(value,age,num)
print(str2)
#{}放数字，就可以控制 顺序
str3='姓名:{2},年龄:{0},爱好:{1}'.format(value,age,num)
print(str3)

#方法3：  format的有个变形      f'{直接放变量}xxx{} yyy{}'
#如果python2的版本，没有  f''  格式化的，只能用str.format()
print('姓名:{value},年龄:{age},爱好:{num}')
print(f'姓名:{value},年龄:{age},爱好:{num}')










