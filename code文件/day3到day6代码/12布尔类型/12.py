#or 是只有一项为True
print(bool(0 or 8))
print(bool(7 or 9))
print(4 and 9)
print(0 or 4)
print(0 or 0 and 1 or 3 and 4 or 3 and 9)
print((0 or 0 and 1 or 3 and 4 or 3) and 9)
#最后回答出4
#需要看优先级
print(0 and 1 and 4 and 9)
print(0 or 0 or 4 or 9)
'''大致如下
正负号   乘除   加减   比较运算   not   and   or   if else'''
