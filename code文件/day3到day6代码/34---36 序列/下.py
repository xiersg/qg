#all() any()
#一个判断全为真  一个判断部分为真
x = [1,1,0]
print(all(x),any(x))
y = [1,11,9]
print(all(y),any(y))

#enumerate()  将可迭代对象每个元素及其序号（从0开始）组成一个二元组列表
s = ["spring","summer","fall","winter"]
S = list(enumerate(s))
print(S)
'''还可以设定开始的值'''
S  = list(enumerate(s,10))
#序号从10开始
print(S)

'''zip() 将多个可迭代对象聚合成元组'''
x = [1,2,3,4,5]
y = "niumo"
z = ["n","m","k"]
a = list(zip(x,y,z))
print(a)
#会以最短的为主
'''使用 itertools 中的 itertools.zip_longest()可以以长的为主'''
import itertools
a = list(itertools.zip_longest(x,y,z))
print(a)

'''map(计算方法，计算对象)对可迭代对象进行计算'''
结果 = list(map(ord,"FishC"))
print(结果)
print(pow(2,5))
q = list(map(pow,[2,3,5,7],[6,3,7,5]))
print(q)
#简化计算
'''长度不一致时'''
print(list(map(max,[2,8,8],[2,4,7],[3,6,9,5])))
#如上，忽略了5

'''filter() 通过计算，将计算结果为真的元素，以迭代器的形式返回'''
print(list(filter(str.islower,"FishC")))


'''迭代器一次性   可迭代对象可以多次操作'''
a = map(pow,[2,3,5,7],[6,3,7,5])
for i in a:
    print(i)
print(list(a))

'''iter() 使可迭代对象变成迭代器'''
x = [1,2,3,4,5]
y = iter(x)
print(y)
print(list(y))
print(tuple(y))
print(type(x))
print(type(y))
'''迭代器专用 next'''
y = iter(x)
for i in range(5):
    print(next(y))
#print(next(y)) 会报错
y = iter(x)
for i in range(6):
    print(next(y,"没啦"))
    
