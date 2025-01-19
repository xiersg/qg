#元组 (可以将括号去掉)
r = (1,2,3,4,5)
print(r)
R = [r[i] for i in range(len(r))]
print(R)
print([r[i] for i in range(len(r))])

#元组的下表索引
for i in range(5):
    print(r[i])

#元组不可变,如：
'''r[1] = 1
   print(r)'''
#但是可以进行更改
r = (1,2,3,4,5,6)

#元组可以进行切片
R = r[:]
print(R)
R1 = r[::2]
print(R1)
R2 = r[1:5:1]
print(R2)
R3 = r[::-1]
print(R3)


#查 count index
num = (2,3,5,3,6,3,5,23)
#count可以查询数量
x = num.count(3)
#index可以查询索引值
y = num.index(3)
print(x,y)

#元组加乘,嵌套
w = 2,3,4,5
e = 7,8,9,9
print(w + e)
print(w * 3)
print(w,e)

#不存在元组推导式，只有生成器

#将元组转化为列表
print(r)
R = []
for i in r:
    R.append(i)
print(R)
#其他看2
    
