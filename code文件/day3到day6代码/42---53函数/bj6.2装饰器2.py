import time

#多重装饰器
def a1(func):
    def xx():
        x = func()
        return x + 1
    print(xx)
    return xx

def a2(func):
    def xx():
        x = func()
        return x*x
    print(xx)
    return xx

def a3(func):
    def xx():
        x = func()
        return x*x*x
    print(xx)
    return xx

@a1
@a2
@a3
def test():
    return 2

print("\n",end = f"{test}\n")
print(test())


#逻辑
'''
关键在于返回
先执行a3，将2返回给x，但是此时xx不执行
再执行a2，将8返回给x,依次类推
最后将函数返回给test，完成装饰器
'''


#给装饰器传递参数
def a1(msg):
    def time_master(func):
        def call_func():
            start = time.time()
            time.sleep(1)
            func()
            end = time.time()
            print(f"[{msg}]一共花了{(end-start)}秒的时间")
        return call_func
    return time_master

@a1(msg="A")
def funcA():
    for i in range(10000):
        for i2 in range(10000):
            continue
            
@a1(msg="B")
def funcB():
    for i in range(10000):
        for i2 in range(10000):
            a = 0

funcA()
funcB()


#实现逻辑
def funcA():
    for i in range(10000):
        for i2 in range(10000):
            continue

funcA = a1(msg = "A")(funcA)
funcA()




#实现传递funcA上参数  
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
