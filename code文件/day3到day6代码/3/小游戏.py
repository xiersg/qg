print('----------甲鱼工作室爱我--------')
纳西妲 = input('是几呢，猜猜看吗') 
#input要求用户输入，并将输入值赋予 纳西妲
guess = int(纳西妲)
#将参数 纳西妲 化为整形输入guess
if guess == 8:
    print("猜中，但无奖")
    print("怎么猜的教我")
#因为同一缩进，所以同一等级
else:
    print('猜错了噢')
    print("美妙的时光总有镜头")
#若不是，则打出猜错了
print("游戏结束")
