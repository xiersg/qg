x = input("请输入主序列")
y = input("请输入子序列")
for i in y:
    if i not in x:
        print("不是其子序列")
        break
else:
    print("是其子序列")
