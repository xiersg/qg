#改
d = dict.fromkeys("FishC")
print(d)
d["s"] = 0
print(d)
#多改
#update方法
d.update({"i":199,"h":190})
print(d)

#查
#直接索引查  若没有会报错
#grt 方法
d.get('c',"这里没有")
#setdefault方法  若存在于字典中，后面的参数没有意义
d.setdefault("c",56)
d.setdefault("C",78)
print(d)
print()
#如果没有，则会添加

#items keys values  视图对象 键+值 键 值
print(d.keys(),d.values(),d.items())

