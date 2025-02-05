import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import sys
sys.path.append(r"D:\qg文件\day11\pythonProject1\.venv\data_read.py")
import data_read as dr
data = dr.data

#不同年龄段乘客生还几率
age_range = data["Age"]
print(age_range.min(),age_range.max())
#人数
age_num,_ = np.histogram(age_range,range=[0,80],bins = 16)#分为16区间，忽略返回的区间边界值
print(f"各年龄段人数{age_num}")
#生还人数
age_huo = []
for age in range(0,76,5):
    survived_num = data.loc[(age_range>=age) & (age_range<=age+5)]['Survived'].sum()
    age_huo.append(survived_num)
print(age_huo)

plt.figure(figsize = (12,6))#尺寸
plt.bar(np.arange(2,78,5)+0.5,age_num,width = 5 ,label = "总人数",alpha = 0.8,color=(0.66,0.87,0.45))
#alpha透明度
plt.bar(np.arange(2,78,5)+0.5,age_huo,width = 5,label="生还人数",color=(0.87,0.12,0.15))
#将将256位真颜色转化为RGB值
plt.xticks(range(0,81,5))
plt.yticks(range(0,121,10))
plt.xlabel("年龄",position = (0.95,0),fontsize = 15)#x轴标签
plt.ylabel("人数",position = (0,0.95),fontsize = 15)#y轴标签
plt.title("各年龄阶段人数，生还人数条形图")
plt.grid(True,linestyle=':',alpha=0.6)#网格线
plt.show()