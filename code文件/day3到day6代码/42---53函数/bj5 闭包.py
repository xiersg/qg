def x():
    a = 0
    b = 0
    def y(a1,a2):
        nonlocal a,b
        a += a1
        b += a2
        print(a,b)
    print(a,b)
    return y


'''
Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: D:/小甲鱼python/42---53函数/bj5 闭包.py
q = x()
0 0
q
<function x.<locals>.y at 0x000001CDE9328220>
q(1,2)
1 2
q(1,3)
2 5
x()
0 0
<function x.<locals>.y at 0x000001CDE9328360>
q(0,0)
2 5
w = x()
0 0
w(1,2)
1 2

'''
