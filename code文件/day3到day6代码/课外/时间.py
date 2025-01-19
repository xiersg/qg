import time

def time_master(func):
    def call_func():
        print("开始运行程序...")
        start = time.time()
        func()
        stop = time.time()
        print("结束程序运行")
        print(f"一共耗费了 {(stop - start):2f} 秒")
    return call_func
