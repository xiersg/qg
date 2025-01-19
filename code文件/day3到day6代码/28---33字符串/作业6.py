x = input("输入")
if len(x)%2 != 0:
    print('无法转化')
else:
    y = list(x)
    a = []
    for i in range(len(x)//2):
        a.append(y[i])
        a.append(y[i+len(x)//2])
    print(''.join(a))
    
a,b,z = [],[],[]
for i in x:
    if i.isdecimal():
        a.append(i)
    else:
        b.append(i)
if abs(len(a)-len(b))>1:
    print('无法转化')
else:
    if len(a)>len(b):
        for i in range(len(b)):
            z.append(a[i])
            z.append(b[i])
        z.append(a[-1])
    else:
        for i in range(len(a)):
            z.append(b[i])
            z.append(a[i])
        z.append(b[-1])
print(''.join(z))
            
    
    
