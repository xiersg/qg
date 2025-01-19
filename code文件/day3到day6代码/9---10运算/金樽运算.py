import decimal
a = decimal.Decimal('0.1')
b = decimal.Decimal('0.2')
print(a + b)


#数字上加不加引号计算结果不一样
import decimal
a = decimal.Decimal(0.1)
b = decimal.Decimal(0.2)
print(a + b)

#python会采用科学计数法的形式
'''会输出2e-09,即为2*10的负九次方'''
print(0.000000002)

#复数，数学中i用j来表示   如：2 + 4j
x = 2 + 4j
print(x.real)
print(x.imag)
#一个实部一个虚部
