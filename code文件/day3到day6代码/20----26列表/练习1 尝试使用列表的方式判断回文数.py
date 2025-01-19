#回文数6---列表
输入 = input('请输入一个整数')
s1 = float(输入)
s2 = s1 % 1
while s2 != 0:
    输入 = input('请输入一个整数!!!')
x = list(输入)
y = x[::-1]
if x == y:
    print('是回文数')
else:
    print('不是回文数')

    
