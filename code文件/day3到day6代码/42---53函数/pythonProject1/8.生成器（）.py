#想要保存函数中数据
'''闭包 全局变量'''
"""简单又安全的 方法，生成器"""
def counter():
    i = 0
    while i <= 5:
        yield i
        i+=1

print("调用函数得到的不再是返回值，而是生成器对象\n counter() = {}".format(counter()))

#使用生成器
for i in counter():
    print(i)
print("for 语句每次运行，从一个可迭代对象里获取一个数据 而counter每次提交一个数据")
print("每次执行到yield的时候，暂停并保留数据，下一次调用从下一个语句开始执行\n")

#生成器作为一种特殊的迭代器，支持next函数,一次提供一个数据
c = counter()
for i in range(6):
    next(c)
print("不能使用下标索引。\n")

#使用生成器实现斐波那契数列
def fib():
    back1,back2 = 1,1
    while(1):
        back1,back2 = back2,back1+back2
        yield back1
f = fib()
for i in range(int(input("请输入想要获取的斐波那契数列"))):
    print(next(f))
#或者
f2 = fib()
i2 = int(input("或者，输入："))
for i in f2:
    print(i)
    i2 -= 1
    if i2<=0:
        break

print("\n\"元组表达式构建生成器\"")
a = (i*i for i in range(10))
for i in a:
    print(i)

def fac():
    while (1):
        j,k = 1,2
        yield j
        j,k = j*k,k+1
fa = fac()
n = int(input("\n输入："))
a = [next(fa) for i in range(n) if i>0]
print(a)
