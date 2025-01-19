print('----------甲鱼工作室爱我--------')

import random
answer = random.randint (1,10)
x = 3
y = 1
while y == 1:
    while x > 0:


        纳西妲 = input('是几呢，猜猜看吗\n') 
        #input要求用户输入整数，并将输入值赋予 纳西妲
        guess = int(纳西妲)
        #将参数 纳西妲 化为整形输入guess
        if guess == answer:
            print("猜中，但无奖")
            break
            #x = -999
            #可以使用   break  跳出一层循环体系
        else:
            if guess < answer:
                print('猜错了噢')
                print("\n大概小了点，再试试？")
            else:
                print('猜错了噢\n\n大概大了点，再试试？')
            #若不是，则打出猜错了
            x = x-1
    if x > 0:
        print('不玩了再见')
    else:
        print('还没猜到啊，真没意思')
        x = 3



'''新语法  '''
# while 注意在条件后加上冒号
#break  跳出循环


''' 新语法'''
#伪随机数生成  random模块
#先要，导入模块   import random
#再设定随机整数闭区间范围
#                 random.randint(x,y)
#可以将随机数的值赋予变量
#                 X = random.randint(x,y)


''' random.randint(x,y)的攻击 '''
#现将他的状态赋予变量
#                 Y = random.getstate()
#后来再将状态逆转
#                 random.setstate(Y)
#OK
