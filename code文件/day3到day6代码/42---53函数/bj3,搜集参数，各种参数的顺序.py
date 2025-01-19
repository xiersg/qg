#收集参数、
#类似print()想要输入几个参数都可以

def myfunc(*args):
    print("有{}个参数".format(len(args)))
    print("第二个参数是：{}".format(args[1]))
    print(args)
    print(type(args))

#收集参数会自动变成一个元组
#应用了元组打包和解包的能力


#如果在收集参数后还要加其他参数  则  需要使用关键字参数来输入  否则会被纳入到收集参数中
def x(*arg,a,b):
    print("a = {},b = {}".format(a,b))
    print(arg)
    

#上一节课的伏笔
def y(a,*,b):#限制了 * 后面只能使用关键字参数   #并且不能无限输入
    pass


#收集参数还可以将参数打包为字典  两个连续的 * 星号
def z(**kwargs):
    print(kwargs)


#普通参数可以放在收集参数之前，字典收集参数放在普通收集参数之后
def g(a,*b,c,**d):
    print("a = {}\nb = {}\nc = {}\nd = {}".format(a,b,c,d))
#普通收集参数一定要在字典收集参数之前  不能有两个字典收集参数或者普通收集参数
#  format()函数就是含有两个 一个* 和 两个*的函数
#此种  *   和   **    可以选择不输入


#还可以使用解包传入参数
age = (1,2,3,4)
def f(a1,a2,a3,a4):
    print(a1,a2,a3,a4)

#尝试 f(age)会报错  而尝试   f(*age)   则会对age进行解包 传入参数
#同理可以i、将字典前加上两个**从而进行解包


#还要检验一下默认参数
#综上，1.位置参数  2.收集参数  3.关键字参数  4.关键字收集参数   (默认参数在关键字收集参数之前)

def f(a,b=5,c=6):
    print(a,b,c)
f(1,2)








    
