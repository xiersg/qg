import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import sys
sys.path.append(r"D:\qg文件\day11\pythonProject1\.venv")
import data_read as dr
data = dr.data
import fare1_survived as fs
fare_death = fs.fare_death
survived_rate = fs.survived_rate

#根据不同票价计算死亡率
death_rate = fare_death["Number"].div(fare_death["Total"])
death_rate = pd.DataFrame(death_rate)
death_rate.columns = ["death_rate"]
death_rate.index = fare_death["Fare"]
print(death_rate)

# 两张散点图画在同一张图纸上
plt.figure(figsize = (21,12))
axes1 = plt.subplot(2,2,1)
axes1.scatter(survived_rate.index,survived_rate,marker = "o",color = (0.32,0.98,0.45))
axes1.set_title("乘客生还率和票价关系的散点图")

axes2 = plt.subplot(2,2,2)
axes2.scatter(death_rate.index,death_rate,marker = "^",color = (0.78,0.63,0.54))
axes2.set_title("乘客死亡率和票价关系散点图")

axes3 = plt.subplot(3,1,3)
fare_death = data.loc[data["Survived"] == 0]
fn_range,_ = np.histogram(data["Fare"],range = [0,263],bins = 180)
fd_range,_ = np.histogram(fare_death["Fare"],range = [0,263],bins = 180)
print(fn_range)
print(fd_range)

plt.bar(np.arange(2,898,5)+0.5,fn_range,width = 5,label = "票价——总人数",alpha = 0.5,color = (0.66,0.87,0.45))
plt.bar(np.arange(2,898,5)+0.5,fd_range,width = 5,label = "票价——死亡人数",color = (0.87,0.12,0.15))
plt.xticks(range(0,263,25))
plt.yticks(range(0,200,10))
plt.xlabel("价格",position = (0,263,180),fontsize = 15)#x轴标签
plt.ylabel("人数",position = (0,15,180),fontsize = 15)#y轴标签
plt.title("各价格人数，生还人数条形图")
plt.grid(True,linestyle=':',alpha=0.6)#网格线
plt.show()
