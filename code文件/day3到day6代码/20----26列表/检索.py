a = ['1','2','3','4','5','牛魔']
x = input('搜索')
if x in a:
    print(x,'在列表a中')
else:
    print(x,'不在列表中')


a = ['1','2','3','4','5','牛魔']
x = input('搜索')
y = list(x)
if all(element in a for element in y):
    print(x,'在列表a中')
else:
    print(x,'不在列表中')









