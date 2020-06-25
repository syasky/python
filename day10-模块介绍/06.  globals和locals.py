
#查看  当前可用的 全局变量或者局部变量

a=1
b='abc'

# print(globals())

def funcA():
    c=[1,2,3]
    d={'a':10}
    print(locals())
    print(globals())

funcA()


#自己调用自己
import time
def sayStory():
    time.sleep(1)
    print('今天给大家将一个故事')
    time.sleep(1)
    print('从前有座山')
    time.sleep(1)
    print('山里有座庙')
    time.sleep(1)
    print('庙里有个老和尚给小和尚讲故事')
    time.sleep(1)
    print('讲的是什么呢')
    sayStory()

sayStory()





