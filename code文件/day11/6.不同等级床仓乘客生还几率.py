import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import sys
sys.path.append(r"D:\qg文件\day11\pythonProject1\.venv\data_read.py")
import data_read as dr
data = dr.data

#不同等级生还率可视化
pclass_count = data.groupby(by="Pclass")["Survived"].value_counts()
print(pclass_count)

plt.figure(figsize = (12,6))
axes1 = plt.subplot(1,3,1)
axes1.pie(pclass_count.loc[1][::-1],autopct = "%.2f%%",labels =["死亡","活着"],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15),colors=[(0.49,0.52,0.89),(0.51,0.87,0.97)],startangle=45)
axes1.set_title("一等舱乘客生还率")

axes2 = plt.subplot(1,3,2)
axes2.pie(pclass_count.loc[2],autopct = "%.2f%%",labels =["死亡","活着"],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15),colors=[(0.49,0.52,0.89),(0.51,0.87,0.97)],startangle=45)
axes2.set_title("二等舱乘客生还率")

axes3 = plt.subplot(1,3,3)
axes3.pie(pclass_count.loc[3],autopct = "%.2f%%",labels =["死亡","活着"],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15),colors=[(0.49,0.52,0.89),(0.51,0.87,0.97)],startangle=45)
axes3.set_title("3等舱乘客生还率")

plt.show()
