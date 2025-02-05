import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import sys
sys.path.append(r"D:\qg文件\day11\pythonProject1\.venv\data_read.py")
import data_read as dr
data = dr.data


#不同港口生存人数
embarked_num = data.groupby(by = "Embarked")["Survived"].value_counts()
print("打印各港口生存人数",embarked_num)
plt.figure(figsize = (20,7))

axes1 = plt.subplot(1,3,1)#第一幅图
axes1.pie(embarked_num.loc["C"][::-1],autopct = "%.2f%%",labels=["死亡","存活"],pctdistance= 0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15),colors=[(0.13,0.56,0.43),(0.75,0.89,0.32)],startangle=45)
#上面之所以加上[::-1]切片反转是因为数据01顺序不一定一致，有一些需要翻转过来,以匹配上死亡存活标签
axes1.set_title("法国瑟堡市乘客生还率")

axes2 = plt.subplot(1,3,2)#第二
axes2.pie(embarked_num.loc["Q"],autopct="%2.f%%",labels = ["死亡","存活"],pctdistance= 0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15),colors=[(0.13,0.56,0.43),(0.75,0.89,0.32)],startangle=45)
axes2.set_title("爱尔兰昆士敦乘客生还率")

axes3 = plt.subplot(1,3,3)
axes3.pie(embarked_num.loc["S"],autopct = "%.2f%%",labels = ("死亡","活着"),pctdistance= 0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15),colors=[(0.13,0.56,0.43),(0.75,0.89,0.32)],startangle=45)
axes3.set_title("英国南安普顿乘客生还率")
plt.show()