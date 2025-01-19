#列表5  引用
x = [1,2,3]
y = x
x[1] = 3
print(y)
print(x)


#浅拷贝  copy  切片
x = [1,2,3]
y = x.copy()
x[1] = 3
print(x)
print(y)
#切片
x = [1,2,3]
y = x[:]
x[1] = 3
print(x)
print(y,'\n')
#用不了的时候（嵌套列表）
x = [[1,2,3],[4,5,6],[7,8,9]]
y = x.copy()
x[1][1] = 0
print(x,'   ',y)
#只能拷贝一层
x = [[1,2,3],[4,5,6],[7,8,9]]
y = x.copy()
x[1] = 1
print(x,'   ',y)


#拷贝copy模块 
import copy
x = [[1,2,3],[4,5,6],[7,8,9]]
#浅拷贝
y = copy.copy(x)
x[1][1] = 0
print(x)
print(y)
#深拷贝
x = [[1,2,3],[4,5,6],[7,8,9]]
y = copy.deepcopy(x)
x[1][1] = 0
print(x)
print(y)
