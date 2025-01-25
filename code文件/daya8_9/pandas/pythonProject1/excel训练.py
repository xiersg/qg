import pandas as pd

file = r"D:\wechat机器人\name.xlsx"
file2 = r"D:\wechat机器人\name_px.xlsx"
data = pd.read_excel(file, sheet_name='JIA', header=0)
'''
pd.read_(object)读取一个类型的文件，转化为pandas类型
sheet_name 表示获取excel文件中的项目
header 读取1行以上的
'''

print(data)
#会看到行索引和列索引
#获取列索引和行索引
print("列索引--",data.columns)
print("行索引--",data.index)

#选择列
select_col = data['生物']
print("type(select_col) = ",type(select_col),'\n',select_col)
#选择多列
select_cols = data[['生物','评价']]#需要两个括号
print(select_cols)

#选择多行多列  data.iloc[:,:]前选行，后选列
print("\n\n多行多列选择")
Acol = data.iloc[0:3,0:3]
print(Acol)
print("\n\n")

#选择某一行
print("\n\n\\n\n\n\n\n")
select_line = data.loc[[3]]
print(select_line)
'''loc 接收具体的行索引  iloc接收具体的行列索引'''
#选择某些行
sel_line = data.loc[[1,3,5]]
print(sel_line)


#数据运算
data['价比'] = data['评价']/data['价格']
print(data)


#排序
data.sort_values(by = 'sequence')
print("\n\n排序",data)
#inplace 指的是是否改变原来的变量
data.sort_values(by = '价比',inplace = True)
print("\n\n排序",data)


#保存
data.iloc[:,1:].to_excel(file2,sheet_name = "JIA_new",index = False)

#详细数据查看
print(data.info())