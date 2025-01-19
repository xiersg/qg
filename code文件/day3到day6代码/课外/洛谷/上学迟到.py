s = int(input("s"))
v = int(input("v"))

t = s/v
if t % 1 != 0:
    t+=1

t = int(t)

t2 = 480
t1 = t2 - t -10
sx = t1//60
fz = t1%60
print("{}:{}".format(sx,fz))
