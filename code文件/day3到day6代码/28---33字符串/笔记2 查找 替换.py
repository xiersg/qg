#查找
#count(sub,start,end)
#使用count查找后，找到过一次的所有字符都会被忽视 如 '11111'.count('11') == 2w
x = '上海自来水来自海上'
y = x.count('海')
print(y)
y = x.count('海',0,5)
print(y)
#find rfind(sub,start,end) 定位 一个从左往右一个放过来
y1 = x.find('海')
print(y1)
y2 = x.rfind('海')
print(y2)
#index rindex(sub,start,end)
'''和 find rfind 很相似，不同在于索引不到时的处理不同'''
print(x.find('龟龟'))
print(x.rfind('龟龟'))
#以下会出错
#print(x.index('龟龟'))


#替换
#expandtabs 将Tap转化为空格
b = '''
\tprint(I love FishC)
    print('I love lin')'''
print(b)
b2 = b.expandtabs(4)
print(b2)
#replace 字符串转化 replace(旧，新)
hj = '在吗！我在你家楼下，下来！！'
xhj = hj.replace('在吗','起床')
print(xhj)
#translate(table) 替换  ()中，1 2为替换，3为删除相关字符
table = str.maketrans('ABCDEFG','1234567','love')
r = 'I love FishC'
R = r.translate(table)
print(R)
