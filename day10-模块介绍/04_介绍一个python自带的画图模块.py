#turtle
# from turtle import *


import turtle as t

t.pd()    #落笔
t.pensize(5)  #线条宽度
colors='red,orange,yellow,green,cyan,blue'.split(',')

# for i in range(6):
#     t.color(colors[i])    #设置线条颜色
#     t.circle(100)        #画图，半价100
#     t.left(60)           #左转60度
#
# t.done()    #暂停在最后画完的状态


t.right(67.5)
for i in range(4):
    t.color(colors[i])    #设置线条颜色
    t.circle(100,360,4)        #画图，半价100
    t.left(45)           #左转60度

t.done()    #暂停在最后画完的状态