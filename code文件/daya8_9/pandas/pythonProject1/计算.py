import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(5,7),index = [1,2,3,4,5],columns = list("fishcca"))
print(df)
df2 = df.copy()

df2.iloc[2:4,3:5] = None
print("\n",df2)

#操作：
df2[df2>0.1]+=10
print("改变后df2:\n\n",df2)

#去除空项所在列
df3 = df2.copy()
df3.dropna(how="any") #这里不清楚，有机会去了解
print("New df3 = \n",df3 )

#填补空项
df4 = df2.copy()
df4.fillna(value =  9999)
print("New df4 = \n",df4)

#运算
print("\n\nNew df_px = \n",df.mean())
print("New df_px = \n",df.mean(axis = 1))


