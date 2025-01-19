#回文数4
x = input('请输入一个回文数，要求为整数')
y = float(x)
while y % 1 != 0:
    x = input('请输入整数！')
    y = float(x)
z = int(y)
n = len(x)
xuke = 1
for i in range(1,int(n/2) + 1,1):
    #取出两端数字
    a1 = z % 10
    #注意  **  才是次方，而不是^
    a2 = z // (10 ** ((n + 1) - (2 * i)))
    print(a1,a2)
    #判断取出数字是否相等
    if a1 != a2:
        xuke = 0
        break
    #除去两端数字
    else:
        xuke = 1
        z = z % 10 ** ((n + 1) - (2 * i))
        z = z // 10
        print(z)
if xuke == 1:
    print('是')
else :
    print('否')



#回文数其五
x = input('请输入一个回文数，要求为整数')
y = float(x)
while y % 1 != 0:
    x = input('请输入整数！')
    y = float(x)
z = int(y)
n = len(x)
a = 1
x1 = 0
y1 = 0
if n == 1:
    print('yes')
while a <= n/2:
    a += 1
    x1 = z % 10
    y1 = 10 * y1
    y1 = y1 + x1
    z = int(z // 10)
    print(z,y1)
if n % 2 == 1:
    z = z // 10
if y1 == z:
    print('yes')

