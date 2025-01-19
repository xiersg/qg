#列表的  增删改查

#增
#append  添加在最后
heros = ['绿巨人','黑寡妇','钢铁侠']
heros.append('蜘蛛侠')
print(heros)
#extend  添加在列表末尾，可以加入一个可迭代对象（目前可以看作列表）
heros.extend(['鹰眼','灭霸','雷神'])
print(heros)
#变量[len(变量)：] = [需要加入的项]
x = [1,2,3,4,5]
x[len(x):] = [6,7,8]
print(x)
x[8:] = [9]
print(x)
#insert(a,b)  可在任意位置添加列表  a为索引值位置，b为加入的项
x = [1,3,4,5]
x.insert(1,2)
print(x)


#删
#remove   如果列表中有多个匹配的元素，则只会删除第一个  如果指定元素不存在，则会报错
heros.remove("灭霸")
print(heros)
#pop(a)   a为元素索引值,假如未指定参数，将会删除最后一个
heros = ['绿巨人', '黑寡妇', '钢铁侠', '蜘蛛侠', '鹰眼', '灭霸', '雷神']
a = heros
heros.pop(len(heros)-1)
print(heros)
a.pop()
print(a)
print(heros)
#clear  消灭所有 = del heros[:]
heros.clear()
print(heros)
print(a)
#del()
heros = ['绿巨人', '黑寡妇', '钢铁侠', '蜘蛛侠', '鹰眼', '灭霸', '雷神']
del(heros[0:2])
print(heros)
