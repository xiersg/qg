x = 'FishCcCode'
y = list(x)
print(y)
for i in range(len(y)):
    if i >= len(y)-1:
        break
    if y[i].swapcase() == y[i+1]:
        y.pop(i)
        y.pop(i+1)
x = ''.join(y)
print(x)
print()

#创建一个符合要求的字符串
import random
a = []
for i in range(3):
    a.append(random.randint(1,10))
    a.append(random.randint(97,123))
for i in range(1,len(a),2):
    a[i-1] += a[i]
    if a[i-1] > 122:
        a[i-1] -= 26
    a[i],a[i-1] = chr(a[i]),chr(a[i-1])
x = "{}{}{}{}{}{}".format(a[0],a[1],a[2],a[3],a[4],a[5])


