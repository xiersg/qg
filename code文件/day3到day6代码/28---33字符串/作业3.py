x = "I love FishC and FishC love me"
y = input('搜索')
z = []
for i in range(len(x)):
    if x.startswith(y,i) == True:
        for i2 in range(i,len(x)):
            if x.startswith(y,i,i2) == True:
                z.append([i,i2])
                break
print(z)   

#判断是否为重复字符串
输入 = input('请输入一个字符串用以判断是否为重复字符串')
#注意切片为 x[::]
for i in range(1,len(输入)):
    if len(输入) % i== 0:
        if 输入[0:i] * int((len(输入)/i)) == 输入:
            print('True')
            break
else:
    print('False')
        
#检测是否全为字母
#isalpha() 方法判断的 “字母” 是 Unicode 编码中定义的字母，不止是 26 个英文字母哈^o^()
s = input('输入')
print(输入.isalpha() and 输入.isascll())
#isascll 方法检测是否为ASCLL编码
