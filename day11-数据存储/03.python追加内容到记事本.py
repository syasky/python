
#mode=a
file =open('1.1.txt','a',encoding='utf-8')
data=['123','武当山','456','真的溜']

#两种方法写入
#方法1
#for each in data:
#     file.writ(each)


#方法2
file.writelines(data)

#如果想让每个字符串占一行，方法一比较实用
for each in data:
    file.write(each+'\n')

file.close()














