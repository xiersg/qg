#推导式构建列表
S = [[0] * 3 for i in range(3)]
print(S)
S[1][1] = 1
print(S)

L = ['Fishc','Appf','object','bool']
for i in L:
    I = list(i)
    if I[0] == 'f' or I[0] == 'F':
        print(i)
print()

L = ['Fishc','Appf','object','bool']
for l in L:
    I = [i for i in l]
    print(I)
print()

#列表推导式进阶
L = ['Fishc','Appf','object','bool']
S = [w for w in L if w[0] == 'f' or w[0] == 'F']
print(S)
print()

#列表推导式嵌套
#使列表降维
a = [[0] * 3 for i in range(3)]
b = [e for e1 in a for e in e1]
#从左到右进行执行
print(b)
print()
#换位
b = []
a = [[0] * 3 for i in range(3)]
for e in a:
    for e1 in e:
        b.append(e1)
print(b)
print()

#嵌套列表推导式的顺序 由左到右且为循环一样的执行
print([x + y for x in 'fishc' for y in 'FISHC'])

a = [[0] * 3 for i in range(3)]

