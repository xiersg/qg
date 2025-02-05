import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import sys
sys.path.append(r"D:\qg文件\day11\pythonProject1\.venv\data_read.py")
import data_read as dr
data = dr.data

print("不同票价乘客生还率")
fare_count = data.groupby(by = "Fare")["Survived"].value_counts()
#根据票价区分存活和死亡的人数
fare_count = pd.DataFrame(fare_count)
fare_count.columns = ["Number"]#将默认名count改为Number
fare_count.reset_index(inplace = True)
print(fare_count)

print("统计出的各票价乘客总人数")
fare_num = fare_count.groupby(by = "Fare")["Number"].sum()#票价人数
fare_num = pd.DataFrame(fare_num)
fare_num.rename(columns = {"Number":"Total"},inplace = True)
print(fare_num)

#存活下来人的数据
fare_survived = fare_count.loc[fare_count["Survived"] == 1]
fare_survived = fare_survived.merge(fare_num,left_on = "Fare",right_index = True,how = "inner")
print(fare_survived)

#各票价乘客生还率
survived_rate = fare_survived["Number"].div(fare_survived["Total"])#相除得生还率
survived_rate.index = fare_survived["Fare"]
survived_rate = pd.DataFrame(survived_rate)
survived_rate.columns = ["survival rate"]#给计算数据列命名
print(survived_rate)

#死亡人数
fare_death = fare_count.loc[fare_count['Survived']==0]#筛选出死亡得
fare_death = fare_death.merge(fare_num,left_on='Fare',right_index=True,how='inner')
print(fare_death)



