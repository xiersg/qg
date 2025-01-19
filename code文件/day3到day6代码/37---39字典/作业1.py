print("欢迎使用FishC影评小程序")
print('1.录入\n2.查询\n3.退出')
zi = []
x = int(input("选择功能"))
while True:
    if x == 1:
        yi = []
        name = input("电影名字")
        yi.append(name)
        time = input("上映时间")
        yi.append(time)
        yi.append(input("导演名字"))
        yi.append(input("演员名字"))
        yi.append(input("电影评分"))
        zi.append(yi)
    if x == 2 :
        ne = input("搜索内容")
        for i in range(len(zi)):
            if ne in zi[i][0]:
                print(zi[i])
        else:
            print("无")
    if x==3:
        break
    x = int(input('选择功能'))
        
        
