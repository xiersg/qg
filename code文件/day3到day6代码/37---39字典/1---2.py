'''字典'''
'''映射关系'''
#1.列表相同位置索引获取对应关系
#2索引值加1
#3字典
'''字典实操'''
x = {"吕布":"牛魔","关羽":"大牛魔"}
#左键右值
print(x["吕布"])

'''加入新的映射关系'''
x["刘备"] = "刘牛魔"
print(x)

'''创建字典'''
'''#1 如上'''
'''#2 dict'''
b = dict(吕布 = '牛魔',关羽 = "大牛魔",刘备 = "刘牛魔")
print(b)
#键上不能加引号
'''#3列表作为参数'''
c = dict([("吕布","口口布"),("关羽","大牛魔"),("刘备","刘牛魔")])
print(c)
'''无病呻吟版'''
d = dict({"吕布":"牛魔","关羽":"大牛魔"})
#应该用不上，不如直接第一个
'''混合法'''
e = dict({"吕布":"牛魔","关羽":"大牛魔"}, 刘备 = "刘牛魔")
'''6 zip'''
f = dict(zip(["吕布","关羽","刘备"],["牛魔","大牛魔","刘牛魔"]))
#zip函数将可迭代对象转化为迭代器，可以使用 tuple()  list()  str()等方式将其输出
#此处 dict() 将其转化为字典


print()
print(x,'\n',b,'\n',c,'\n',d,'\n',e,'\n',f)
print(bool(x == b == c == d == e == f))



print("\n\n\n\n{}\n\n\n\n".format(f))



#增
#fromkeys(iterable,[values])
a = dict.fromkeys("FishC",250)
a["F"] = 70
print(a)
print()

#获取视图对象
#keys()键  values()值  items()键和值   方法
A = a.keys()
print(A)
B = a.values()
print(B)
C = a.items ()

print(C)
#字典同列表一样，需要使用拷贝来复制
e = a.copy()
print(e)
print(len(a))

#使用 in   not in判断建是否存在于字典中
print("F" in a)
#值不可以

#转化为列表
print(list(a))
#以键组成的列表
print(list(a.keys()))
#同上一个
print(list(a.values()))
print(list(a.items ()))

#使用iter生成迭代器
i = iter(a)
print(i)

#使用reversed()翻转
print(list(reversed(a.values())))

#嵌套
q = {"吕布":{"语文":60,"数学":70,"英语":80}}
print(q["吕布"]["数学"])

#字典推导式
print()
print(a)
o = {x:y for x,y in a.items() if y>100}
print(o)
ords = {x:ord(x) for x in "FishC"}
print(ords)















