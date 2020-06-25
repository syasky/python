
# break 终止所在循环
#输出 range(1,20) 当大于5时，终止
for i in range(1,20):
    if i>5:
        break
    print(i)

#continue 跳过当前这次continue后的语句，开始下一次循环
#输出 range(1,20) 跳过10-15
for i in range(1,20):
    if 10<=i<=15:
        continue
    print(i)

#pass 是为了保证循环结构完整
for each in range(10):
    pass


