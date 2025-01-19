print("{:-^10}".format("录入模式"))
zd = {}
while True:
    print("1:录入 / 2:查询 / 3.删除 / 4:打印 / 5:退出")
    xz = int(input("功能"))  
    if xz == 1:
        mz = input("请输入名字 ：")
        dh = input("号码")
        z = ""
        while len(z) !=11 or dh.isdecimal == False:
            z = input("请输入11位仅含数字的手机号码")
        for i in zd:
            if mz == i:
                print("以存在，是否更换")
                q = input("【Y/N】")
                if q == "Y":
                    zd[i] = dh
                break
        else:
            zd[mz] = [dh]
        zd[mz] = z
    elif xz == 2:
        mz = input("想要搜索的人")
        for i in zd:
            if mz in i:
                print(f"名字:{i}\n电话号码:{zd[i]}")
        else:
            print("没有更多的了")
    elif xz == 3:
        mz = input("想要搜索的人")
        for i in zd:
            if mz in i:
                zd.pop[i]
                print("完成")
        else:
            print("没有更多的了")
    elif xz == 4:
        mz = input("想要搜索的人")
        for i in zd:
            if mz in i:
                print(f"{i}:{zd[i]}")
    elif xz == 5:
        break
        
