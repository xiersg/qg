print(10.55)

#正常除法，取得浮点数
print(10/3)

#地板除，向下取整
print(-10//3)

#取模
print(10%3)

#绝对值
a = abs(-7.85)
print(a)
#另，若a = 复数，输出的是复数的模（实部和虚部的平方平均数）
b = 5 + 3j
print(abs(b))

#int会将浮点数转换为整数直接截取
int(5.66)

#float会转化为浮点数
print(float('3.14'))
print(float('3'))
#e记法
print(float('5e6'))

#domplex转化复数。需要注意的是complex不能加空格
print(complex('2+3j'))

#幂运算
print(pow(3,10))
print(3 ** 10)
#另pow支持三个参数
d = pow(3,10,2)
print(d)
e = 3 ** 10 % 2
print(e)
