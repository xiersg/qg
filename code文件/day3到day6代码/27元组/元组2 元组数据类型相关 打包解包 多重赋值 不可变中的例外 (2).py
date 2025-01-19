#建议一直加上圆括号
r = (1,2)
print(type(r))
#元组 tuple
R = list(r)
print(R)
print('反之')
r = tuple(R)
print(r)
print()

print('检验')
rt = type(r)
print(rt)
Rt = type(R)
print(Rt)
print()

#生成一个元素的元组
x = (33,)
print(type(x))

#打包 解包
#打包可以认为是生成一个元组
x = (2.33,'希儿',3.14)
#解包将元组内元素分别赋值给变量
a,b,c = x
print(a,b,c)
#同理，其实很多都可以这么做
x = '希儿'
a,b = x
print(a,b)
print()
x = [0,1,2,3,4]
a,b,c,d,e = x
print(a,b,c,d,e)
#注意，解包时左侧变量数和右侧元素数要求 相同
#否则，要
x = (2.33,'希儿',3.14,520,'牛魔')
a,b,*c = x
print(a)
print(b)
print(c)

#多重赋值
a,b,c = 1,2,3
print(a,b,c)
#通过元组打包解包实现
_ = 1,2,3
a,b,c = _
print(1,2,3)

#元组不可变中的可变
q = [1,2,3]
e = [4,5,6]
w = (q,e)
print(w)
w[0][0] = 000
print(w)


