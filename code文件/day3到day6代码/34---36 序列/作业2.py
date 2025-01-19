a = []
b = []
x = input("请输入整数，自动转化为整数列表")
while x.isdecimal == False:
    x = input("整数")
x = list(x)
for i in x:
    if int(i) % 2 == 0:
        a.append(i)
    else:
        b.append(i)
a = sorted(a)
b = sorted(b)
print(a+b)
