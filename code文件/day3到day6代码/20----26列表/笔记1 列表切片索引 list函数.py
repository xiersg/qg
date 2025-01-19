#创建列表
x = [1,2,3,4,5]
print(x)
#第一项为0，依次推
print(x[2])
#[-1]为最后一项
print(x[-1])
#或者，使用
n = len(x)
print(x[n-1])

#列表切片   形式:  列表变量[num1:num2]   取左不取右
y = [1,2,3,4,5,6,7,8,9,10,11]
print(y)
z = y[3:6]
print(z)
#列表切片2  形式：列表变量[:]  列表变量[:num]   列表变量[num:]:::::::所有  从头开始   从num开始
print(y[:])
print(y[:3])
print(y[3:])
#列表切片3  形式：列表变量[num1:num2:num3]  1开始，2结束，跨度为3  ***取左不取右***
print(y[1:9:1])
#还可以：     原理同上
print(y[::2])
print(y[::])
#也可以
print(y[::-1])
print(y[::-2])

#使用list可将字符串转化为列表
z = "philosophy"
z1 = list(z)
print(z1)
n = len(z1)
print(n)
print(z1[3])
