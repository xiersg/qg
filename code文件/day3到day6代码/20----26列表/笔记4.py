s = 123456
s_str = str(s)
s_list = [int(i) for i in s_str]
print(s_list)

t = 7890
t_str = str(t)
t_list = [int(i) for i in t_str]
print(t_list)

print(s_list + t_list)

#列表矩阵
matrlx = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrlx)
for i in matrlx:
    for each in i:
        print(each,end = ' ')
    print()

#矩阵下标索引
print(matrlx[0][1])

#矩阵构建，矩阵初始化
A = [0] * 3
for i in range(3):
    A[i] = [0] * 3
print(A)
#错误示范
B = [[0] * 3] * 3
print(B)
#看似一样，实则不同  使用is
a = [1,2,3]
b = [1,2,3]
print(a is b)
c = 'Fishc'
d = 'Fishc'
print(c is d)
#因为字符串不可变，而列表可变所以列表即使内容相同，也需要存放于不用两个位置，使得si的结果为False
#依次，验证
print(A[0] is A[1])
print(B[0] is B[1])









