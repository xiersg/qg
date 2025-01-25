import numpy as np

#传入可迭代对象
a = np.array([1,2,3,4,5])
b = np.zeros([3,3])
b = np.zeros((5),dtype = np.int32)
c = np.ones([4,4])
c = c.astype(np.int8)
d = np.arange(1,9)
e = np.random.rand(3,9)
f = np.linspace(0,1,12)
#默认类型为64位浮点数，可以更改
'''
a = np.zeros((4,2))
类型有：
    np.int8/16/32/64
    np.uint8/16/32/64
    np.float------
    bool
    str
'''

print(a,"\n\n",b,"\n\n",c,"\n\n",d,"\n\n",e,"\n\n",f)
print("尺寸！=", a.shape,b.shape,c.shape,d.shape,e.shape)

#数学运算
print("a+b = ",a+b)
print("a*b = ",a*b)
print("np.dot(a,b) = ",np.dot(a,b))
print("a@b = ",a@b)
print("np.log(a) = ",np.log(a))
print("np.sqrt(a) = ",np.sqrt(a))
print("np.power(a,3) = ",np.power(a,3))
print("sin cos tan",np.sin(a),np.cos(a),np.tan(a),np.arcsin(a),np.arccos(a),np.arctan(a))
#上面的代码会因为范围不对而警告

#广播和扩展
"""
如 a*5
如 a*c,不同尺寸进行运算
"""

print("a.max a.argmax a.min a.argmax ")
print("np.median(a)中位数  a.mean()平均值")
print("a.sum")
print("a.var()方差  a.std()标准方差")
print(e.sum(axis = 0))
print(e.sum(axis = 1))
print(d)
print(d[(d>3) & (d%2 == 0)])
print(d[(d>3)|(d%2 == 0)])
