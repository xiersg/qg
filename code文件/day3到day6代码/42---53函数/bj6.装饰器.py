#装饰器
#原理：将函数1转化为参数传入函数2，在将函数2返回给函数1，执行函数1就同时执行了函数1和函数2

#引用time库 计算时间
import time


#装饰器原理1
def time_master(func):
    print("开始执行程序...")
    start = time.time()
    func()
    stop = time.time()
    print("函数运行结束...")
    print(f"一共耗费了{(stop-start):.3f}秒。")

def x1():
    time.sleep(0.5)#time.sleep可以使函数停止一定时间
    temp = 0
    for i in range(100):
        for i2 in range(100):
            temp += i*i2
    print("共{}".format(temp))

time_master(x1)


print("-----——————-----")


#装饰器原理2
def time_master2(func):
    def call_func():
        print("开始执行程序...")
        start = time.time()
        func()
        stop = time.time()
        print("函数运行结束...")
        print(f"一共耗费了{(stop-start):.3f}秒。")
    return call_func

#x1如上定义

x1 = time_master2(x1)
x1()


print("-----——————-----")


#装饰器语法糖
def time_master2(func):
    def call_func():
        print("开始执行程序...")
        start = time.time()
        func()
        stop = time.time()
        print("函数运行结束...")
        print(f"一共耗费了{(stop-start):.3f}秒。")
    return call_func

@time_master2
def x1():
    time.sleep(0.5)#time.sleep可以使函数停止一定时间
    temp = 0
    for i in range(100):
        for i2 in range(100):
            temp += i*i2
    print("共{}".format(temp))

x1()


print("-----——————-----")
