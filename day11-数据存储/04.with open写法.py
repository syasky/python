
# with open 可以代替 普通的open写法

file=open('2.txt',mode='w',encoding='utf-8')
file.write('12345')
file.close()


#不需要写关闭，脱离with结构自动关闭
with open('2.txt',mode='w',encoding='utf-8') as file2:
    file2.write('\n')
    file2.write('678910')















