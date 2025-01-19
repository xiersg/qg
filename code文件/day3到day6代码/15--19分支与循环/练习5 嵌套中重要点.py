#for in
for each in "niumo":
    print(each)
#range(a,b,c)  a为开始 b为结束 c为跨度
for i in range(4,50,3):
    print(i,end = " ")
print("\n")


#等差求和 Sn = Sn-1 + An
sum = 0
x = 1
for i in range(1,100100,1):
        sum = sum + i
print(sum)

#寻找质数
for a in range(1,11,1):
    for b in range(2,10,1):
        if a == b:
            continue
        if a % b == 0:
            print(a,'不是质数')
            break
    else:
        print(a,'是质数')
print(' ')
#寻找质数2,想使用all解决
'''for a in range(1,a + 1,1):
    xy = 0
    for b in range(2,10,1):
        if a % b != 0 and a != b:'''

#寻找质数3（甲鱼专享）
for c in range(1,10):
    for d in range(2,c):
        if c % d == 0:
            print(c,'不是质数')
            break
    else:
        print(c,'是   质   数')

#改进自己的
for a in range(1,11,1):
    for b in range(2,10,1):
        if a == b:
            continue
        if a % b == 0:
            print(a,'不是质数')
            break
    else:
        print(a,'是质数')
print(' ')
        
