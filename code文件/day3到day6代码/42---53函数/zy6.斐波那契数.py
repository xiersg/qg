import time



n = int(input("输入想要获取的斐波那契数个数"))



def get_fib(n):
    for i in range(n):
        fib()

def time_master(func):
    a = func()
    def func2():
        x = time.time()
        a()
        y = time.time()
        if (y - x) < 0:
            time.sleep(1-(y-x))
    return func2

@time_master
def fib():
    back1,back2 = 0,1
    def func():
        nonlocal back1,back2
        back1,back2 = back2,back1+back2
        print(back1,end = "  ")
    return func

get_fib(n)
