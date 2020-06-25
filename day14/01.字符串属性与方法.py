
#1. string.capitalize()      首字母大写
print('welcome'.capitalize())

#2. string.center(width,填充的东西)
print('welcome'.center(20,'喵'))

#3. string.count(str,beg=0,end=len(string))
str3='咪喵喵喵喵喵咪喵喵喵喵咪喵喵喵喵喵喵咪喵喵喵喵喵喵咪喵'
print(str3.count('咪'))
print(str3.count('喵'))
print(str3.count('喵',5))    #从第5个开始数

#4. decode()
#   encode()
#假设一个场景，你是一个特务，你需要加密情报
mibao='今晚回家吃3个鸡腿'
print(mibao)
jiami=mibao.encode('gbk')
print(jiami)

#接头人接到mibao,他需要解密
jiemil=jiami.decode('gbk',errors='ignore')
print(jiemil)

jiemi2=jiami.decode('utf-8',errors='ignore')
print(jiemi2)

# 5. string.startswith(str,begin,end )检查 string[begin:end] 内是否以str开头# string. endsmidth(str,begin,end)检查string[begin:end] 内是否以str结尾
#假设有一个列表，有很多人的名字在里面
names = ['熊大','熊二','张雷','李雷','王五','小北喵','熊孩子']
#找出所有姓熊的
#用学过的
result =[each for each in names if each[0]=='熊']
print (result)
result2 =[each for each in names if each. startswith('熊')]
print (result2)

print([each for each in names if'喵' in each])

# 6.string.expandtabs(tabsize=8) 将字符串汇总的 tab 转为空格，默认8个
str6='a\tb\tc'
print(str6)
print(str6.expandtabs(0))
print(str6.expandtabs(10))

#7.string. find(str,start,end )
#寻找str在string[start:end] 内出现的str在整个string中的下标
#找到则返回索引，找不到返回-1
str7 = '大吉大利，今晚吃鸡'
print( str7.find('大') )
print( str7.find('大',2,-1))   #大利，今晚吃鸡
print( str7.find('大',3,-1))   #利，今晚吃鸡

#练习： 假设有个长字符串，秘密在 前两个@@ 中间，请打印除秘密
mimi='asiufhskjnfiush@天王盖地虎@ahifushfnsdufhsnfsjhiufhjhuish'

#找到第一个@的下标
first=mimi.find('@')
#找到第二个@的下标
second=mimi.find('@',first+1)
#用字符串截取的方式输出
print(mimi[first+1:second])

# 8. string.index(str ,start ,end )  同 find ,找不到会报错
print('abcde'.find('h'))
# print('abcde'.index('h'))

# 9  string.isalnum()  判断 string内是否 完全 由数字字母（包括汉字）组成
print('abc123'.isalnum())
print('abc123哈哈'.isalnum())
print('abc123哈哈--'.isalnum())

# 10 .   string.islower() 判断是否有字母且字母为纯小写.
print('123'.islower())
print('A123'.islower())
print('a123'.islower())

# 11. string.join(seq)
str11 = '天地玄黄'
print('¤'.join(str11))
# 将日期转为 str
timelist = ['2020','5','21']
print(  '/'.join(timelist))

#  12.    string.lower()  全部转为小写
#         string.upper() 全部转为大写

# 13. string.strip(x) 返回去除 string两边 的 x 后的字符串，默认去除空格
#  string.lstrip(x) 返回去除 string 左边 的 x 后的字符串，默认去除空格
#  string.rstrip(x) 返回去除 string 右边 的 x 后的字符串，默认去除空格
str13 = '  abc   '
print(str13.strip())
print(str13.lstrip())
print(str13.rstrip())

str13 = '|abcd|'
print(str13.strip('|'))
str133 = '|-123abc-%|'
print( str133.strip('|').strip('%').strip('-') )

#  14.   string.replace(old ,new ,n )
#  将 string内的 old 替换成  new 字符， n 次 .默认所有
str14 = 'abc-abc-abc-abc'
# 将 a 替换成 A
print( str14.replace('a','A'))
print( str14.replace('a','A' ,1))
print( str14.replace('a','HAHAHAHAHA' ,1))

# 15. string.split( str = '' ,num= string.count(str))
#使用 string 中的 str 作为 分隔符，分割 string,返回 list 。 num 为分割此处，默认所有
str15 = '东邪,西毒,南帝,北丐'.split(',')
print(str15)
# 分割2次
print( '东邪,西毒,南帝,北丐'.split(',', 2))




