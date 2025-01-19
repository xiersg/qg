L = [[1 ,2 ,3 ,4 , 5],
     [6 ,7 ,8 ,9 ,10],
     [11,12,13,14,15],
     [16,17,18,19,20],
     [21,22,23,24,25]]
x = 1
y = 0
a = 1
b = 1
c = 0
while True:
    x += a
    y += b
    if x == 0 or x == len(L[y]) - 1:
        a = - a
    if y == 0 or y == len(L) - 1:
        b = - b
    print(L[y][x])
    c += 1
    if c == 10:
        c =  0
        po = input("继续")
    

