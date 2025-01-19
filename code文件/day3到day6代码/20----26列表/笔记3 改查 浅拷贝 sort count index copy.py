#改  下标索引
#单改
heros = ['猪猪侠','波比','失败的man','灭霸','烧鸡','人族大帝']
heros[3] = '牛魔'
print(heros)
heros
print(heros)
heros[len(heros):] = ['烧鸡','人族大帝']
print(heros)

#多改
heros[5:] = [""]
print(heros)
del heros[4:]
print(heros)

#排序  sort函数实现排序
nums = [4,5,3,5,6,2,5,4,3,1]
nums.sort()
print(nums)
#reverse函数实现倒转
nums.reverse()
print(nums)
heros.reverse()
print(heros)
#nums.sort(key=None,reverse=True) 
nums = [4,5,3,5,6,2,5,4,3,1]
nums.sort(reverse=True)
print(nums)





#查
#count  查次数
x = nums.count(5)
print(x)

#index 查下标  index只会寻找范围内下标最小的一个
heros = ['猪猪侠','波比','失败的man','灭霸','烧鸡','人族大帝','华强']
y = heros.index('失败的man')
print(y)
#还可以运用于：
heros[heros.index('失败的man')] = '自助侠'
print(heros)
#还可以使用  x.index(y,a,b)   y为查找对象  a为开头  b为结尾  依旧取左不取右
x = [3,3,3,3,4,3,3,3,4]
y = x.index(4,4,)
print(y)
x = [3,3,3,3,4,3,3,3,4]
y = x.index(4,5,9)
print(y)


#拷贝
#浅拷贝 copy   列表是不能使用变量的赋值方法的，直接赋值会使两个-- --共同指向同一列表
print(nums)
nums_copy1 = nums.copy()
print(nums_copy1)
#可以以 nums[:]的形式（切片）达成目的  浅拷贝
nums = [6, 5, 5, 5, 4, 4, 3, 3, 2, 1]
nums1 = nums[:]
print(nums1)
