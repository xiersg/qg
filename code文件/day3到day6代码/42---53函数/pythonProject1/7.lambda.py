#一行流 lambda

# lambda arg1,arg2----- argn : expresssion lambda表达式
'''对比'''
def squ(x):
    return x**2
squ2 = lambda y:y**2
print("squ(3) =",squ(3))
print("squ2(4) =",squ2(4))

#传统函数的函数名为函数的引用 而 lambda表达式为函数的引用
a = [squ,squ2]
print(a[0](3))
print(a[0](5))

#但是，lambda表达式为函数的引用 <- 因为这样 可以直接将lambda表达式放在列表里
b = [lambda y:y**3,lambda y:y**4,lambda y:y**5]
print("将lambda表达式直接放入列表进行引用：")
for i in range(3):
    print(f"b[{i}](3) = {b[i](3)}]")
print()

#lambda 搭配 map 举世无双
"""map有两个参数 第一个是函数 第二个是一个序列类型 map进行处理后 生成一个迭代器"""
print("将lambda放入map,加密通讯")
a = input("请输入一串字符")
b = int(input("请输入加密数字"))
A = "".join(list(map(lambda x,y = b : chr(ord(x)+y),a)))
print(A,"\n")