n = int(input("数字"))
if n < 2:
    print(0)
elif n == 2:
    print(1)
elif n > 2:
    z = [2]
    for i in range(3,n,2):
        for i2 in z[:len(z)//2:]:#优化 减少遍历个数
            if i % i2 == 0:
                break
        else:
                z.append(i)
    print(len(z))

