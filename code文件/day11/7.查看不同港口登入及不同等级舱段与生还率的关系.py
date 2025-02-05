import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import sys
sys.path.append(r"D:\qg文件\day11\pythonProject1\.venv\data_read.py")
import data_read as dr
data = dr.data


plt.figure(figsize = (21,12))
#不同等级生还率可视化
pclass_count = data.groupby(by="Pclass")["Survived"].value_counts()
print(pclass_count)

axes1 = plt.subplot(3,3,1)
axes1.pie(pclass_count.loc[1][::-1],autopct = "%.2f%%",labels =["死亡","活着"],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15),colors=[(0.23,0.87,0.42),(0.49,0.52,0.89)],startangle=45)
axes1.set_title("1等舱乘客生还率")

axes2 = plt.subplot(3,3,4)
axes2.pie(pclass_count.loc[2],autopct = "%.2f%%",labels =["死亡","活着"],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15),colors=[(0.23,0.87,0.42),(0.49,0.52,0.89)],startangle=45)
axes2.set_title("二等舱乘客生还率")

axes3 = plt.subplot(3,3,7)
axes3.pie(pclass_count.loc[3],autopct = "%.2f%%",labels =["死亡","活着"],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15),colors=[(0.23,0.87,0.42),(0.49,0.52,0.89)],startangle=45)
axes3.set_title("3等舱乘客生还率")



#纵向对比第二行
#不同港口生存人数
embarked_num = data.groupby(by = "Embarked")["Survived"].value_counts()
print("打印各港口生存人数",embarked_num)

axes21 = plt.subplot(3,3,2)#第一幅图
axes21.pie(embarked_num.loc["C"][::-1],autopct = "%.2f%%",labels=["死亡","存活"],pctdistance= 0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15),colors=[(0.46,0.76,0.45),(0.51,0.87,0.97)],startangle=45)
axes21.set_title("法国瑟堡市乘客生还率")

axes22 = plt.subplot(3,3,5)#第二
axes22.pie(embarked_num.loc["Q"],autopct="%2.f%%",labels = ["死亡","存活"],pctdistance= 0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15),colors=[(0.46,0.76,0.45),(0.51,0.87,0.97)],startangle=45)
axes22.set_title("爱尔兰昆士敦乘客生还率")

axes23 = plt.subplot(3,3,8)
axes23.pie(embarked_num.loc["S"],autopct = "%.2f%%",labels = ("死亡","活着"),pctdistance= 0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15),colors=[(0.46,0.76,0.45),(0.51,0.87,0.97)],startangle=45)
axes23.set_title("英国南安普顿乘客生还率")


#纵向对比第三行,不同港口登入的人进入不同等级舱段的比例
embarked_pclass = data.groupby(by = "Embarked")["Pclass"].value_counts()
print(embarked_pclass)

axes31 = plt.subplot(3,3,3)
axes31.pie(embarked_pclass.loc["C"],autopct = "%.2f%%",labels=['一等舱','三等舱','二等舱'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1,0.1],textprops=dict(size=15),colors=[(0.98,0.57,0.11),(0.32,0.93,0.27),(0.42,0.42,0.77)])
axes31.set_title("法国瑟堡市乘客舱段等级分布")

axes32 = plt.subplot(3,3,6)
axes32.pie(embarked_pclass.loc["Q"],autopct='%.2f%%',labels=['三等舱','二等舱','一等舱'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1,0.1],textprops=dict(size=10),colors=[(0.32,0.93,0.27),(0.42,0.42,0.77),(0.98,0.57,0.11)],startangle=10)
axes32.set_title('爱尔兰昆士敦乘客舱段等级分布')

axes33 = plt.subplot(3,3,9)
axes33.pie(embarked_pclass.loc["S"],autopct='%.2f%%',labels=['三等舱','二等舱','一等舱'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1,0.1],textprops=dict(size=15),colors=[(0.32,0.93,0.27),(0.42,0.42,0.77),(0.98,0.57,0.11)],startangle=180)
axes33.set_title("英国南安普顿乘客舱段等级分布")

plt.show()