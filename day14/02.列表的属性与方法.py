
#某班级有 个小组
group='张三,李四,王五,赵六'.split(',')

#去上体育课
#七娃跑到队伍的结尾
#list.append(obj)   将obj追加到list结尾
group.append('七娃')
print(group)

#火影里来个鸣人，分身术，一次性结尾增加三个 鸣人
#list.extend(seq)  将seq中的对象 一次性放入到list结尾
group.extend(['鸣人','鸣人','鸣人'])
print(group)

#动漫中的 熊大和熊二也来凑热闹，排成 大，二，三 。。。，也就是插队
#list.insert(index,value) 将value插入到list的index索引位置
group.insert(0,'熊大')
print(group)
group.insert(1,'熊二')
print(group)

#老师一看怎么有这么多鸣人，数数有几个
#list.count(obj) 返回list中obj的数量
num=group.count('鸣人')
print(num)

#又来了个八娃，想在七娃后面
#总需要知道七娃在哪个索引吧
#list.index(obj) 返回obj在list中索引
index7=group.index('七娃')
#再使用insert
group.insert(index7+1,'八娃')
print(group)

# 下课了,队伍里的人要 回 动漫世界去了
# list.pop()  默认删除 list结尾的对象
# list.pop(index)  删除 index 索引的对象
#  del  list[idnex]  删除 index 索引的对象

# 队伍的最后2人撤了
group.pop()
group.pop()
print(group)

# 队伍的第一个人撤了
group.pop(0)
print(group)

#  把 队伍 中 不肯走的熊二，扔掉
# list.remove(obj)  list 移除指定对象 ，不管你在哪儿的
group.remove('熊二')
print(group)

# 老师向后转， 往前走，相对于整个队伍倒序了
#  list.reverse()
group.reverse()
print(group)

#  体育课的成绩 张三-鸣人
import random
data = [random.choice(range(60,100)) for each in range(7)]
print('成绩：',data)

# 将成绩排序
# list.sort(reverse= 0/1) 0 代表升序 ，1 代表降序 ，默认 0
data.sort(reverse=1) # 更改原数据
print(data)

# 老师想看从小到大的成绩
# data.reverse()
# print(data)

print( data[::-1])

#========================
# 现在  ['张三', '李四', '王五', '赵六', '七娃', '八王爷', '鸣人'] 的语数外成绩如下
team = ['张三', '李四', '王五', '赵六', '七娃', '八娃', '鸣人']
# score =  [[team[i]]+[ random.choice(range(60,100)) for i in range(3)] for i in range(7)]
# 假设           语   数   英
score = [['张三', 88, 62, 78],
         ['李四', 83, 88, 92],
         ['王五', 70, 64, 60],
         ['赵六', 88, 82, 92],
         ['七娃', 62, 66, 95],
         ['八娃', 97, 78, 99],
         ['鸣人', 68, 83, 91]]
print(score)
# list.sort(key=xxx  ,reverse=True/False)
# xxx 一般是个数字
# 可以是整个数字 list 的每项处理后的数字 ,用函数处理,将每项当成参数传入.最终的返回值

# 这个xxx 数字可以是 某门成绩 ，也可以是某几门成绩计算出来的

# 如按照语文成绩 排序
def funA(x):
    return x[1]
# score.sort(key= funA )
# 用 匿名函数
score.sort(key=lambda x:x[1])
print(score)


# 按照 总成绩排序
score.sort(key=lambda x:sum(x[1:]))





