#序列
#字符串  列表  元组
#共同点 1.切片 2.索引值从0开始 3.索引获取元素

#运算符
# + *
print([1,2,3] + [4,5,6])
#元组字符串都可以
x = [0]*3
for i in range(3):
    x[i] = [0]*3
print(x)

#增值运算
x = [1,2,3]
y = (1,2,3)
z = '1,2,3'
x *= 2
#增值运算时使用 乘法 加法 列表id值不会改变，而正常加乘不会
y *= 2
z *= 2
print(x,y,z)

#id值 相当于身份证
#三大基本属性：唯一标识，类型，数值
#is   is not  用于判断id值是否相同
x = [1,2,3]
x2 = x+x
print(x is x2)
x3 = x * 2
print(x is x3)
print()
#列表相关陷阱
x=[1,2,3]
y = x
print(x is y)
print(x == y)
#2
x=[1,2]
y=[1,2]
print(x is y,x==y)

#in   not in 判断是否包含
print("鱼" in "鱼C")

#del 删除
x = [1,2,3,4,5,6]
y = '1,2,3'
del y
#删除y
del x[0:2]
print(x)
#切片大法
x1 = [1,2,3,4,5,6]
x1[0:2] = []
print(x1)
print(x1 is x,x1 == x)
print()
#clear del 对比
y = [1,2,3,4,5]
print(y.clear())
y = [1,2,3,4,5]
del y[::]
print(y)
#直接删除  打印错误
del y
try :
    print(y)
except Exception as e:
    # 这里处理错误，可以打印错误信息或者记录日志
    print(f"An error occurred: {e}")
print()
#跳过错误
y = []
del y
try:
    print(y)
except Exception:
    pass  # 忽略这个异常
