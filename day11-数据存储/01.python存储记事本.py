
#1.打开文件，存在则打开，不存在则创建打开
#open(fileName,mode='' ,encoding='')
#fileName:文件名
# mode:模式  默认 r=read    ,  w:write     , a:append

#此处写入用 mode='w'   清空并写入
file =open('1.0.txt',mode='w',encoding='utf-8')

#2.写入内容
# file.write(str)
file.write('12345\n')
file.write('678910')

# file.writelines(可迭代的存字符串组成的数据)
file.writelines(['abc','一二三'])

#3.保存关闭
file.close()


#===============================================
#特殊需求，我想写入的数据中有  \n
#mode='wb'   ,没有 encoding参数 ，所有字符串  都是  b'str'的形式
file2 = open('1.1.txt',mode='wb')
file2.write(b'12345\n')
# \\n ,可以写入\n
file2.write(b'\\n')
file2.write(b'6789\n')
file2.close()