import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import sys
sys.path.append(r"D:\qg文件\day11\pythonProject1\.venv\data_read.py")
import data_read as dr

data = dr.data
#不同性别乘客生还可视化
sex_huo = data.groupby(by = "Sex")["Survived"].value_counts()
print("不同性别生还",sex_huo)
plt.figure(figsize=(2*5,5))#窗口大小

axes1 = plt.subplot(1,2,1)#创建两个图，一个1行
axes1.pie(sex_huo.loc["female"][::-1],autopct="%.2f%%",labels = ["死亡","存活"],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15),colors=['#9400D3','#FFB6C1'],startangle=90)
axes1.set_title("女性生还率")

axes2 = plt.subplot(1,2,2)
axes2.pie(sex_huo.loc["male"],autopct="%.2f%%",labels=["死亡","存活"],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15),colors=['#9400D3','#FFB6C1'],startangle=90)
axes2.set_title("男生还率")
plt.show()