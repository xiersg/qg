print("欢迎来到鱼c小程序")
print("1.录入\n2.查询3.退出")
x = int(input("选择功能"))
xx = []
zd = {}
while True:
    if x == 1:
        xx,mz = [],""
        mz = input("电影名字")
        xx.append(input("时间"))
        xx.append(input("导演名字"))
        xx.append(input("演员名字"))
        xx.append(input("评分"))
        zd[mz] = xx
    if x == 2:
       n = input("查询的电影名字")
       for i in zd:
           if n in i :
               print(f"电影名字:{i}")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                
    if x == 3:        break
    x = int(input("功能"))
