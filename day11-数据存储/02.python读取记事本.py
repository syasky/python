
#mode='r'
#1.打开文件
# file=open('1.0.txt',mode='r',encoding='utf-8')
#2.读取  file.read(n),没有 n 读取所有
# print(file.read())

#连续读取 是  接着 读    （换行也算一个字符）
# print(file.read(4))
# print(file.read(4))
# print(file.read(5))

#3.关闭
# file.close()

#============================================
#mode='rb'   , 不需要encoding参数
# \n  \r  会直接读取
# file2=open('1.0.txt',mode='rb')
# print(file2.read(10))
# print(file2.read(3))
# file2.close()


#======================================
#mode='r+' 读写
# file3=open('1.0.txt',mode='r+',encoding='utf-8')
# file3.write('0')
#将数据  输入 文件
# file3.flush()
# print(file3.read(3))
# file3.close()

#读取 的 其他内容
#file.read()按照字节读取                                    返回字符串
#file.readline(n) 按行读取     有n就是返回这一行的n个字符 ，没有就返回这行全部    返回字符串
#file.readlines（）读取所有行                           返回列表
#file.tell()  读取指针位置
#file.seek(n)   移动指针到第n的位置

file4=open('1.1.txt',mode='r',encoding='utf-8')
#file.read()按照字节读取
# print(file4.read(3))
#file.readline() 按行读取
# print(file4.readline())
# print(file4.readline())
# print(file4.readline())

#file.readlines（）读取所有行
# print(file4.readlines())

file4.seek(10)
print(file4.tell())
print(file4.read(1))