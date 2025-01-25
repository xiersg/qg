import pandas as pd

file = r"D:\wechat机器人\name.xlsx"
file2 = r"D:\wechat机器人\name3.xlsx"
file3 = r"D:\wechat机器人\name_hb.xlsx"

data = pd.read_excel(file,sheet_name = "JIA",header = 0)
data2 = pd.read_excel(file2,sheet_name = "JIA",header = 0)

data = data.iloc[:,1:]
print("data = \n",data)
print("\n\ndata2 = \n",data2,"\n\n")

#合并======
print("合并操作\n")
data3 = pd.concat([data,data2],axis = 0)
"""  axis参数表示沿着哪个方向进行链接  """
print(data3)

print("\n\n查看数据来源\n")
data3_2 = data3.sort_values("价格")
print(data3.head())

#链接2
print("\n\n新连接\n")
data4_lj = pd.merge(data,data2,how='left',on='评价')
print(data4_lj)

#返回
data3.to_excel(file3,sheet_name = "hb_new",index = False)


