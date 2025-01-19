#7.私有变量

class C:
    def __init__(self,x):
        self.__x = x
    def set_x(self,x):
        self.__x = x
    def get_x(self):
        print(self.__x)

def get(c):
    c.get_x()
    print(c.__dict__)#可以使用 _类__变量名访问

c = C(252)
get(c)
c.set_x(1000)
get(c)


#动态添加属性给以生成对象添加私有变量
print("\n#动态添加属性给以生成对象添加私有变量")
print(c.__dict__)
c.__y = 101
print(c.__dict__)
#可见，在外部这样改不能生成私有变量
print("还可见 _结尾或开头的变量或函数，需要自觉地不去调用")


#c.__dict__是一个字典，可以操作
print("\n字典除了费内存，其他都是优点")
print('那我tm不用字典了！__slots__')
class C:#划分固定大小空间 
    __slots__ = ["x","y"]
    def __init__(self,x,y):
        self.x = x
        self.y = y

c = C(122,100)
c.y = 199
# print(c.__dict__) 试图访问  __dict__都会报错
print(f"没有__dict__了,但是有 __slots__,c.__slots__ = {c.__slots__}\n")

print("尝试动态添加 c.z = 100")
#c.z = 100    报错
#继承自父类的 slots 属性是不会在子类中生效的
class E(C):
    pass
e = E(120,100)
e.y = 111
print(f'e.x = {e.x},e.y = {e.y}')
e.z = 123
print(f"e.z = {e.z},欸？C中的 __slots__ 没有生效?")
#同时，会存在__dict__属性
class F(C):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z
f = F(1,2,3)
print(f.__dict__)

    






