n = int(input(""))
sum = 0
if n < 2:
    print(0)
elif n == 2:
    print("2\n1")
elif n > 2:
    z = [2]
    for i in range(3,10**5,2):
        for i2 in z[:len(z)//2:]:#优化 减少遍历个数
            if i % i2 == 0:
                break
        else:
            if sum + i <= n:
                sum += i
                z.append(i)
            else:
                break
    for i in z:
        print(i)
    print(len(z))
