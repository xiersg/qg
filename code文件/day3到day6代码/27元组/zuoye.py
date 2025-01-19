# 作业 转化矩阵
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
x = len(matrix)
y = len(matrix[0])
mat = [i1 for i in matrix for i1 in i]
mat1 = [mat[i::4] for i in range(y)]
print(mat1)
