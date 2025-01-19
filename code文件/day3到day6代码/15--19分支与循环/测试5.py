sum = 0
x = 1
for i in range(1,100100000,1):
    if x == 1:
        a1 = i
    elif x == 2:
        a2 = i
    elif x == 3:
        a3 = i
    elif x == 4:
        a4 = i
    elif x == 0:
        a5 = i
        sum = a1 + a2 + a3 + a4 + a5 + sum
        a1 = 0
        a2 = 0
        a3 = 0
        a4 = 0
        a5 = 0
    x += 1
    x = x % 5
sum = a1 + a2 + a3 + a4 + a5 + sum    
print(sum)
    
