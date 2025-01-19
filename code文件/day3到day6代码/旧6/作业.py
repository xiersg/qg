x = input('写一个有理数')
xx = float(x)
a = abs(xx)
b =int(a)
c = a - b
if c < 0.5:
    d = b
else:
    d = b + 1
if xx > 0:
    y = d
else:
    y = 0 - d
print(y)
