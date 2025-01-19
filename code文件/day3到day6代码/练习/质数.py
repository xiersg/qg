n = int(input("数字"))
z = [2,3,5,7]
for i in range(7,n,2):
    if i % 3 != 0 and i % 5 != 0 and i % 7 != 0:#优化
        for i2 in z[:len(z)//2:]:#优化 减少遍历个数
            if i % i2 == 0:
                break
        else:
            z.append(i)
print(len(z))

