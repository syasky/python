
#假设大家是  开发网站的，现在有个注册界面

#假设已经从数据库查询出了账号和密码
info={'zhangsan':'zhagnsan123','lisi':'lisi123'}

#定义装饰器函数  判断  输入的账号密码是否存在
def checkInfo(func):
    def wrap():
        #先收集账号密码
        userName,password=func()
        if userName in info.keys():
            print('账号已存在')
        else:
            print('注册成功')
    return wrap

@checkInfo
def regist():
    #用来收集  你输入的账号和密码
    userName=input('请输入账号：')
    password=input('请输入密码：')
    return userName,password
regist()















