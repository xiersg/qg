import pandas as oo
#这里的缩写可以变成一个变量名
import random
import numpy as np

dates = oo.date_range("20210927",periods = 6)
print("创建行索引：\n",dates)

print("\n\n创建随机数DataFrame:")
datas = oo.DataFrame(np.random.randn(6,5),index = dates,columns=list("abcde"))
print("\n\ndatas = \n",datas)
print(type(np.random.randn(1,2))) #numpy库里面的自动构建正太分布的函数，几个参数表示构建几维数组

print("\n\n字典创建DataFrame ， 键为列标签 ， 值为列值\n")
dic_df = {"a" : [11,22,33,44],#使用列表填充数据
          "b":oo.Categorical(oo.Timestamp(str(i)) for i in range(20210101,20210105)),
          "c" :oo.Series(random.randint(1,9),index = list(range(4)),dtype="float32"),
          "d" :oo.array([3,2,2,1],dtype="int32"),
          "e" :oo.Categorical(["tesr","train","test","trian"]),
          "f" :"none"
          }
datas2 = oo.DataFrame(dic_df)
'''字典创建DataFrame需要每个键对应的值数量一致，或者为数量1'''
print(datas2)

#布尔索引
datas2.sort_values(by = "a",inplace = True)
print("\n\n布尔排序\n",datas[datas["a"]>0])

print("\n\n")

a = oo.DataFrame(np.random.randn(10,1),index = [i for i in range(10)],columns = ["a"])
print("a999 = \n",a)
print(a[a["a"]>0.3] )

#筛选
print("\n\n筛选\n")
print(datas2[datas2["e"].isin(["test"])])

