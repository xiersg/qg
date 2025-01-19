#布尔类型
print(bool('250'))
'''大部分都定义为Ture
    定义为False只是少数
    如1、
    None  False
    2.
    值为0的   0  0.0  0j  Decimal(0)  Fraction(0,1)
    3.
    空的序列和集合
    ''  ""  ()  {}  set()  range(0)'''

#另1 == True   0 == False

if bool(250) == True:
    print('250 is True')
else:
    print('250 is False')

a = True + False
print(a)


#逻辑运算
#  and or not
print(not 0)
'''and需要两边为True时才为True
   or只需一边为True,结果就为True
   not会得到一个相反的布尔数'''
