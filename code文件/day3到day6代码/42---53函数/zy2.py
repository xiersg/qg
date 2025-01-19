zhan = []
a = 1
def push():
    zhan.append(int(input("请输入将要压入栈中的值：")))
    for i in range(len(zhan)):
        print(zhan[::-1][i])
def pop():
    if len(zhan) == 0:
        print("已经没了")
    else:
        print(zhan[-1])
        return zhan.pop()

def top():
    if len(zhan) == 0:
        print("已经没了")
    else:
        print(zhan[-1])

def exit():
    a=0
    
while(a):
    x = input("请输入指令(push/pop/top/exit)")
    if x == 'push':
        push()
    elif x == 'pop':
        pop()
    elif x == 'top':
        top()
    elif x == 'exit':
        exit()
