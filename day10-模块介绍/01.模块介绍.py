
#使用自己定义的模块
from mymoudle import mypow
print(mypow(2,3))

import mymoudle
print(mymoudle.mypow(3,3))

#模块文件的命名要注意，符合变量的命名规范
#from 0_test import mysum()  出错   变量不能带_

#模块作为对象，我们可以  以  模块.xxx 使用那个文件内的 函数，类 以及变量
xiaoming=mymoudle.Person('小明',20)
print(xiaoming.name)
print(xiaoming.age)

print(mymoudle.Year)



'''
总结：
    1.模块的命名要符合命名规范
    2.导入模块的方式  import xxx  或者  from xxx import yyy
    3.模块文件内的运行要加  if __name__=='__main__':    判断  就不会影响其他文件
'''

