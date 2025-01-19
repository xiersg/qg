#内置函数
#转换函数  list()  tuple()  str()
x = "niumo"
y = list(x)
z = tuple(x)
print(x,y,z)
print("将元组列表转化为字符串会比较傻")
xy = str(y)
xz = str(z)
print(xy,"  ",xz)

#min() max()  对比传入的参数 比较获取最大和最小值
#用法  min(x,[key,default])  min(a,b,c[,key])
#key用于指定比较函数
s = [1,2,3,4,4,56,6,7,8]
s_min = min(s)
print(s_min)
#若传入的是字符串，将比较编码值的大小
t = "精英黑暗大牛魔，doge"
t_max = max(t)
print(t_max)
#传入空的可迭代对象就会报错
c = []
c_min = min(c,default ="屁，啥都没有，无法找到最小值" )
#使用default,输出指定内容，其中，可以输入数字
print(c_min)

#len() sum()
#len() 有最大可承受范围 64位是  2**63 -1
print(len(range(2**63-1)))
#sum()计算求和
s = [1,2,3,40,0,86]
print(sum(s))
# sum(s,start = y)从y开始加
print(sum(s,start = 100))

#sorted()

s=[1,2,3,4,0,5]
print(sorted(s))
print(s,'\n')
#sorted()进行原地排列 ， 但会产生一个全新的列表，原列表不受影响
#sort()方法会改变源列表
s.sort()
print(s)
#都支持key reverse[决定是否翻转]
#key为指定函数用于比较
d = ["FishC","niumo","牛魔"]
print(sorted(d))
print(sorted(d,reverse=True))
print(sorted(d,key = len))
#sotr 同上 且其为列表专属
print(sorted("FishC"))
#sorted所有序列都可用

#reverased()反向迭代器
s = [9,2,6,8,0]
print(reversed(s))
print(list(reversed(s)))
#倒过来
print(list(reversed("FishC")))
