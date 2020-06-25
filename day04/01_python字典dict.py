
#通过  字典  的方法进行创建
#键不同，值相同
#fromkeys(seq 如: str list tuple,'baidu')
dict1={}.fromkeys(('first','second'),'baidu')
print(dict1)

#读取  字典
#语法： dict['key']
print(dict1['first'])

#
dict2={'name':'张三','age':20,'hobby':['唱','跳','看书']}
print(dict2['name'])
print(dict2['hobby'][0])
# 读取一个  不存在  的  key。 sex，会报错，并可能影响其他程序运行
# print(dict2['sex'])
#  读取  字典的 方法二： dict.get(key)  ,不存在 会返回None，不报错
print(dict2.get('sex'))

#  修改字典
#语法：  dict['key']=value  ,如果存在key，则换值，不存在则增加进去
#如 给dict2增加性别 为 男
dict2['sex']='男'
dict2['age']=21
print(dict2)

#删除操作
#del  dict['key']
del dict2['hobby']
print(dict2)

#可以清空  字典所有数据
#  xxx.clear()
dict2.clear()
print(dict2)
#del dict2 删除整个字典








