#补充  globals()全局变量字典  locals()局部变量字典  变量需要使用引号
x = {'1':'1'}
print("欢迎来到鱼C论坛~~")
def zc():
    print("===========")
    global name
    global mima
    name = input("请输入用户名：")
    if name in globals():
        x = input("已重复，是否更换 yes/no")
        if x == 'no':
            print("已退出，返回0")
            return 0;
    mima = input("请输入密码：")
    print("恭喜，注册成功！")
            
def dl():
    print("===========")
    name_temp = input("请输入用户名：")
    if name_temp in x:
        chance = 3
        while(chance>=0):
            mima_temp = input("请输入密码：")
            if mima_temp == x[name_temp]:
                print("登陆成功！")
                break
            else:
                chance -= 1
    else:
        print("无此账号")

while(1):
    gn = input("===========\n1.注册\n2.登录\n3.退出\n请输入指令：")
    if gn == '1':
        zc()
        x[name] = mima
    elif gn == '2':
        dl()
    elif gn == '3':
        print('===========')
        break
        
                
        
    
    
    
