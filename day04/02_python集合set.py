
# 创建集合    : 无序，不重复
#语法： set1={1,2,3}  或  xxx=set(object)
set1={1,2,3,4}
print(type(set1))

set2={'a',1,(2,3,4)}
print(set2)
#set()创建
set3=set('abcd')
print(set3)

#set() 应用场景，去重(去除重复)
#
person1=['熊大','熊二','熊小']
person2=['熊小','李四']
person3=['王五','李四']
#哪些人被提名？
all=set(person1+person2+person3)
print(all)

#若想用index，需要转为list或tuple
print(list(all)[0])

#但是可以用for 去 迭代
for each in all:
    print(each)


