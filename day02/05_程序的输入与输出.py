
# 输入  语法：  内置函数 input() 得到字符串
# 可以又提示语句  input('请输入')
# a=input('请输入：')
# print(a)
# print(type(a))
#真正使用变量接收 的 数据时，注意数据类型是否需要转换

#输入两个数  用  num1 和 num2 接受，执行 加法计算，输出结果
# num1=input('请输入第一个数：')
# num2=input('请输入第二个数：')
# print('结果是：',float(num1)+float(num2))
# print(f'结果是：{float(num1)+float(num2)}')

#如果输入特殊呢？  想进行各种计算呢，符号由我们自己定
#eval( str)python的内置函数，他会将str 当成python 代码执行
# str2=input('输入：')
# print(eval(str2))
# print(eval('5/2'))

# str3='print(666)'
# eval(str3)

#---------如果 符号也是 单独输入的咋办？
# c=input('输入第一个数：')
# operator=input('请输入符号:')
# d=input('输入第二个数:')
# print(eval(f'{c}{operator}{d}'))

             #等于

# c=input('输入第一个数：')
# operator=input('请输入符号:')
# d=input('输入第二个数:')
# if operator=='+':
#     print(float(c)+float(d))
# if operator=='-':
#     print(float(c)-float(d))
# if operator=='*':
#     print(float(c)*float(d))
# if operator=='/':
#     print(float(c)/float(d))

