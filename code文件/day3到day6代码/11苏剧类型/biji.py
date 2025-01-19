#数据类型'''''''''''python3可以使用汉字为变量
''''''


#整型   使用int
#int直接截断
小甲鱼 = int('303348')
print(小甲鱼)
不是四舍五入 = int(5.77)
print(不是四舍五入)


#e记法
a = 0.000000000000000000000488
print(a)
b = int(5.55e-10)
print(b)

#浮点型''''''''''''整数转化为浮点数采用float
c = '520'
d = float(c)
print(d)


#布尔类型  bool
'''1 = True
0 = False
可以进行计算'''

    
#字符串（使用内置函数str）
f = str(5e30)
print(f)
#如果
str = 50
'''r = str(50)'''
#会报错


#type  判断数据类型
print(type(a))
print(type(3.5))
print(type(True))
print(type('牛莫'))
#isinstance用于判断数据类型是否相同
print(isinstance(222,float))
print(isinstance(c,float))
print(isinstance(c,int))
# -*- coding: utf-8 -*-
a = '小甲鱼'
print(isinstance(a,str))
'''
s 为字符串

s.isalnum()  所有字符都是数字或者字母，为真返回 True，否则返回 False。

s.isalpha()   所有字符都是字母，为真返回 True，否则返回 False。

s.isdigit()     所有字符都是数字，为真返回 True，否则返回 False。

s.islower()    所有字符都是小写，为真返回 True，否则返回 False。

s.isupper()   所有字符都是大写，为真返回 True，否则返回 False。

s.istitle()      所有单词都是首字母大写，为真返回 True，否则返回 False。

s.isspace()   所有字符都是空白字符，为真返回 True，否则返回 False。
         
例如：
>>> s = 'I LOVE FISHC'
>>> s.isupper()
>>> True
'''
