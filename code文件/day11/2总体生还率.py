import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import sys
sys.path.append(r"D:\qg文件\day11\pythonProject1\.venv\data_read.py")
import data_read as dr
#数据可视化
data = dr.data
print("可视化")
huo = data['Survived'].value_counts()
print(huo)

plt.figure(figsize=(6,6))
plt.pie(huo,autopct='%.2f%%',labels=['死亡','存活'],pctdistance=0.4,labeldistance=0.6,shadow=True,explode=[0,0.1],textprops=dict(size=15))
plt.title('总体生还率')
plt.show()