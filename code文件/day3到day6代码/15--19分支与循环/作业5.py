for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            x = a*100 + b*10 + c
            y = (a ** 3) + (b ** 3) + (c ** 3)
            if x == y:
                print(x,'为水仙花数')
else:
    print('无')



'''#回文数2
x = input('请输入一个回文数，要求为整数')
y = float(x)
while y % 1 != 0:
    x = input('请输入整数！')
    y = float(x)
n = len(x)
for y1 in (x):
    for y2 in (x,-1):
        if y1 != y2:
            print('不是回文数')
            break
        else:
            continue
break'''
            

'''#回文数
x = input('请输入一个回文数，要求为整数')
y = float(x)
while y % 1 != 0:
    x = input('请输入整数！')
    y = float(x)   
z = int(y)
n = len(x)
for i in range(n - 1 ,-1,-1):
    x2 = print(x[i],end = '')
y2 = float(x2)
z2 = int(y2)
if z2 == z:
    print("yes")
else:
    print("no")'''


#回文数3
x = input('请输入一个回文数，要求为整数')
y = float(x)
while y % 1 != 0:
    x = input('请输入整数！')
    y = float(x)
n = len(x)
x1 = 0
x2 = n - 1
while x1 < (n - 1) / 2:
    kb1 = (x[x1])
    while x2 > (n - 1) / 2:
        kb2 = (x[x2])
        print(kb1,kb2)
        break
    if kb1 != kb2:
        print('no')
        xuke = 0
        break
    xuke = 1
    x1 += 1
    x2 -= 1
if xuke == 1:
    print('yes')











    























    
    
