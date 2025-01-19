#作用域
import time

while(1):
    i = int(input("1/2/3/4/5/6"))
    #局部变量
    if i == 1:
        a = 10  #全局变量
        def x():
            a = 5  #局部变量定义
            print(a)
            print(id(a))
        x()
        print(a)
        print(id(a))


    #不改变全局变量的情况下
    if i == 2:
        x = 10
        def x2():
            print(x)
        x2()


    #在内部改变全局变量
    if i == 3:
        x = 10
        def y():
            global x   #使变量x作为全局变量
            x = 5
            print("\n{}".format(x))
            print(id(x))
        y()
        print(x)
        print(id(x))


    #嵌套
    if i == 4:
        x = 10
        print(x)
        def z():
            x = 20
            print(x)
            def zz():
                x = 30
                print(x)
            zz()
            print(x)
        z()
        print(x)


    #nonlocal
    if i == 5:
        def aa():
            x = 100
            print(x,id(x))
            def a():
                nonlocal x
                x = 11
                print(x,id(x))
                def b():
                    x = 10
                    print("id(b) == {}".format(id(x)))
                    def c():
                        nonlocal x
                        x = 10
                        print("id(c) == {}".format(id(x)))
                    c()
                b()
            a()
        aa()

    if i == 6:
        break

def a1(msg):
    def time_master(func):
        def call_func(x_temp):
            global x
            x = x_temp
            start = time.time()
            time.sleep(1)
            print(x)
            func()
            end = time.time()
            print(f"[{msg}]一共花了{(end-start)}秒的时间")
        return call_func
    return time_master

@a1(msg = "A")
def funcA():
    global x
    print("当前参数为{}".format(x))
    for i in range(10000):
        for i2 in range(10000):
            continue

funcA(10)
