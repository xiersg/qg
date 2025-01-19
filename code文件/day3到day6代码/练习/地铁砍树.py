终点 = input("输入总终点")
num = int(input("区域个数"))
x = []
for i in range(int(num)):
    start = int(input('起点'))
    end = int(input("终点"))
    x.append([start,end])
x = sorted(x,key = lambda x:x[0])
for i in range(len(x)):
    while x[i][1] > x[i+1][0]:
        x[i][1] = x[i+1][1]
        x.pop(i+1)
    if i >= len(x)-2:
        break
y = 0
for i in x:
    y += (i[1] - i[0] + 1)
s = int(终点) + 1 - y 
print(f"剩余{s}")
