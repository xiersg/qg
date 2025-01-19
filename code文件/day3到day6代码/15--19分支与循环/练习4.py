#循环语句
#else  只有为False时才执行
i = 0
while i < 10:
    print('循环内i的值为',i)
    i += 1
    
else:
    print('循环外i的值为',i)
#不满足条件时，返回值为0，满足条件时使用break跳出循环时，返回值为1

x = 1
y = 1
while y != 10:
    print(x,'*',y,'=',x * y,end = ' ')
    if x == y:
        y += 1
        x = 1
        print(' ')
    else:
        x += 1






