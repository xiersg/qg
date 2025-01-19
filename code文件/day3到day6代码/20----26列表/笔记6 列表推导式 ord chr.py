 #列表推导式


#将列表元素变为原来两倍
#常规方法
x = [1,2,3,4,5]
n = len(x)
print(n)
print(x[4])
for i in range(n):
    y = x[i]
    x[i] = 2 * y
print(x)
'''小提示，负数索引不得超过一次循环'''
#列表推导式
x = [1,2,3,4,5]
y = [i * 2 for i in x]
print(y)



#列表推导式语法结构：
#[expression for tanrget in iterable]
#列表推导式结果一定是列表
x = [i for i in range(11)]
print(x)
y = [i + 1 for i in x]
print(y)
z = [i ** 2 for i in x]
print(z)


#ord  将单个字符串转化为对应的 Unicode
#chr  ord的逆函数
a = [ord(i) for i in '你真是牛魔啊']
print(a)
b = [chr(i) for i in a]
print(b)


#列表推导式 运用:提取出每行第二个数字
matrlx = [[1,2,3],
          [4,5,6],
          [7,8,9]]
x = [matrlx[i][1] for i in range(3)]
print(x)
#或者
x = [i[1] for i in matrlx]
print(x)

#列表推导式 运用：提取左上右下对角线的数字
x = [matrlx[i][i] for i in range(len(matrlx))]
print(x)
#左下右上
x = [matrlx[i][len(matrlx) - i - 1] for i in range(len(matrlx))]
print(x)


