# 函数的参数类型

#1 必备参数
def funcA(x):
    print(x)
funcA('hello')
# funcA()   不给会报错
# funcA(1,2)   给多也不行

# 而且传入的时候也是按顺序的,顺序一定要注意
def showState(name,mood,age):
    print(f'老夫{name},现在心情{mood}，明年{age+1}')
showState('无敌大帅','很好',20)
# showState(20,'无敌大帅','很好')  会报错

#2 关键字参数，在调用函数的时候进行 赋值式 的写法，可以不管顺序
showState(age=20,name='无敌大帅',mood='很好')

# 必备可以和关键字相结合
def showState2(name,mood,age):
    print(f'老娘{name},现在心情很{mood},明年{age+1}岁')
showState2('王五',age=1000,mood='惆怅')

# 特殊的地方是，一旦有个位置开始写关键字参数，后面必须全写
# showState2('王五','惆怅',age=1000)  会报错









