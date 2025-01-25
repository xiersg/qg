import pandas as pd

name1 = pd.read_excel(r'C:\Users\LENOVO\OneDrive\桌面\name')

data = name1.loc[:,['names']]

print(data)