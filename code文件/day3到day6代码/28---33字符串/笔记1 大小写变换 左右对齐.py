x = '1234321'
y = list(x)
print(y)
y = [int(i) for i in x]
print(y)

#字符串是序列
#切片用的好，头发少不了
print('是回文数') if x == x[::-1] else print('不是回文数')

#字符串各种方法
'''大小写变换'''
#将首字母大写，其他小写
x = 'I love FishC'
y = x.capitalize()
print(y)
#全是小写 能处理英文之外的字符
print(x.casefold())
#将单词首字母大写
y = x.title()
print(y)
#将所有字母大小写翻转
y = x.swapcase()
print(y)
#将所有字母变为大写
y = x.upper()
print(y)
#将所有字母变为小写
y = x.lower()
print(y)

'''左中右对其'''
#center ijust rjust(输出长度，fillchar='填充对象')
#输出长度小于源字符串长度则输出源字符串
X = "有内鬼，停止交易"
Y = X.center(4)
print(Y)
#center  中对齐
Y = X.center(10)
print(Y)
Y = X.center(15)
print(Y)
#ljust   左对齐
Y = X.ljust(25)
print(Y)
#rjust   右对齐
Y = X.rjust(25)
print(Y)
#zfill   使用0填充左侧
Y = X.zfill(15)
print(Y)
#选择填充的字符
Y = X.ljust(25,'j')
print(Y)
Y = X.rjust(25,'j')
print(Y)
Y = X.center(15,'j')
print(Y)

