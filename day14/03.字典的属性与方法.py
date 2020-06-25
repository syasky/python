
dict2 = dict(a=1,b=20,c=300)
print(dict2)

# 字典的方法：
# 1 .dict.fromkeys(seq[, val])
dict3 = dict.fromkeys(list('abc') , 233)
print(dict3)

# 2. dict.get( key ,default='')  读取字典，读不到的时候不会报错，用 default
# print( dict2['d']) # 报错，没有 key d
print( dict2.get('d'))
print( dict2.get('d' ,'我是默认值'))

# 3. dict.items()  返回 键值对 组成 元组 的 seq 对象
print( dict2.items() )

# 4. dict.keys()  键们组成的对象
#   dict.values()  值们 组成的对象
print( dict2.keys())
print( dict2.values())

# 5. dict.update(dict2) 将 dict2 的数据更新到 dict中
dict4 = {'e':4 ,'f':5}
dict4.update(dict2)
print(dict4)

# 6. dict.setdefault(key,value)
dict4.setdefault('d','ddddddddd')
print(dict4)

# 7. dict.pop(key) 删除 dict 的 key
dict4.pop('a')
# 8. dict.popitem() 删除结尾
dict4.popitem()
print( dict4 )



