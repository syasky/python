# dic

#语法：  variable ={key1:value1,key2:value2,.....}
#key 不可以相同，是不可变类型。如 数字，字符串，元组
#value   任意数据类型

# 创建空字典
dict1={}

#对字典增加内容
dict1['name']='张三'
print(dict1)

#直接创建有内容的字典
dict2={'name':'李四','language':'python'}

#数字作为key ，比如简单几个 10进制和2进制

dict3={2:10,8:1000}
print(dict3)

# 可以将  二维对象转为 字典
#如(('a',1),('b',2))
dict4=dict((('a',1),('b',2)))
print(dict4)

# 还可以 dict(key1=value1,key2=value2.....)创建
dict5=dict(name=' 王舞',age=20,sex='女')
print(dict5)
