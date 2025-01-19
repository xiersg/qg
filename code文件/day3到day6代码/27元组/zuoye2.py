l = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]]
#碰墙反馈
Y = len(l)   #一层长度
X = len(l[0])#二层长度
x = 0
y = 0
l2 = [] 
while x < X - 1 and l[y][x + 1] != 0:
    l2.append(l[y][x])
    l[y][x] = 0
    x += 1
while y < Y - 1 and l[y + 1][x] != 0:
    l2.append(l[y][x])
    l[y][x] = 0
    y += 1
while x > 0 and l[y][x - 1] != 0:
    l2.append(l[y][x])
    l[y][x] = 0
    x -= 1
while y > 0 and l[y - 1][x] != 0:
    l2.append(l[y][x])
    l[y][x] = 0
    y -= 1
while x < X - 1 and l[y][x + 1] != 0:
    l2.append(l[y][x])
    l[y][x] = 0
    x += 1
l2.append(l[y][x])
print(l2)

#2   wwwwwwww
    
    


    
