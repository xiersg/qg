import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


print("“一个人的死是个悲剧，一百万人的死只是个统计数字”，这是个令人遗憾的偏见与误读 。\n在分析不同数据的过程中，我仿佛看到当时男人们选择留在船上让妇女和儿童先登上救生艇的画面，仿佛看到在船的中下层因为船舱被封锁而无法逃到甲板上的三等舱乘客绝望的眼神。\n而数据分析的结果都印证了电影里的一些桥段并非虚构，而是真实发生过的事情。\n如果再提起《泰坦尼克号》我想到的不只是感人至深的爱情故事，还有危难之中闪烁的人性光辉。\n")

#显示中文
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # Windows 系统可用
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False  # 正确显示负号

data = pd.read_csv(r"train.csv")
print("查看数据\n",data)

print("获取数据类型列的描述统计信息\n",data.describe())
print("查看每一列的数据类型，和数据总数")
data.info()#自行打印，不需要print
