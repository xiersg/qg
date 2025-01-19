def f(i):
    if i<=0:
        return 1
    return f(i-1)*i

n = int(input("输入"))
print("f({}) == {}".format(n,f(n)))