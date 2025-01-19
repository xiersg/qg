print('----------甲鱼工作室爱我--------')
x = 3
while x > 0:


    纳西妲 = input('是几呢，猜猜看吗\n') 
    #input要求用户输入，并将输入值赋予 纳西妲
    guess = int(纳西妲)
    #将参数 纳西妲 化为整形输入guess
    if guess == 8:
        print("猜中，但无奖")
        print("怎么猜的教我")
        x = -999
    #可以使用   break  跳出一层循环体系
    else:
        if guess < 8:
            print('猜错了噢')
            print("\n大概小了点，再试试？")
        else:
            print('猜错了噢\n\n大概大了点，再试试？')
    #若不是，则打出猜错了
        x = x-1
print('不玩了再见')





'''新语法  '''
# while 注意在条件后加上冒号
#break  跳出循环



print('----------甲鱼工作室爱我--------')
x = 3
while x > 0:


    guess = input('是几呢，猜猜看吗\n') 
    #input要求用户输入，并将输入值赋予 纳西妲
    #将参数 纳西妲 化为整形输入guess
    if guess == 8:
        print("猜中，但无奖")
        print("怎么猜的教我")
        x = -999
    #可以使用   break  跳出一层循环体系
    else:
        if guess < 8:
            print('猜错了噢')
            print("\n大概小了点，再试试？")
        else:
            print('猜错了噢\n\n大概大了点，再试试？')
    #若不是，则打出猜错了
        x = x-1
print('不玩了再见')


