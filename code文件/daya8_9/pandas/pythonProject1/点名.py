import random
import pandas as pd


#参数m  1.重复抽取  2.不重复
#参数x  数量
def call(m,x):
    data = pd.read_excel(r'D:\wechat机器人\name.xlsx',sheet_name='123')
    data2 = data['name']#获取名字那一列
    n = len(data2)
    data3 = [data2.loc[i] for i in range(n)]#转化为列表，（因为我不会操作loc[害怕]）
    if m == '重复抽取':
        roster = list(map(int,random.choices(range(0,n),k = x)))
        #创建中奖序列
        sel_ros = [data3[i] for i in roster]
        sel_ros = f"抽奖完成喵Ψ(￣∀￣)Ψ\n--*--{"--*--\n--*--".join(sel_ros)}--*--"
        return sel_ros
    if m == '不重复':
        if x>n:
            return "太多了【火热】,可选数量超过上限"
        roster = list(map(int,random.sample(range(0,n),k = x)))
        # 创建中奖序列
        sel_ros = [data3[i] for i in roster]
        sel_ros = f"抽奖完成喵Ψ(￣∀￣)Ψ\n--*--{"--*--\n--*--".join(sel_ros)}--*--"
        return sel_ros

print(call("重复抽取",15))
print('喵')
print(call("不重复",4))
