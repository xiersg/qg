#组合
class Cat():
    def say(x):
        print("喵喵喵~")
    def ayu(x):
        print(x.y)

class Dog():
    def say(x):
        print("哟吼，我是一只修狗！")
    def ayu(x):
        print(x.y)#承接下面的，将实例化对象的内部属性打印，若不绑定实例化对象，贼找不到Y

        
class Garden:
    c = Cat()
    d = Dog()
    def say(self):
        self.c.say()
        self.d.say()
    


class C():
    c = Cat()
    d = Dog()
    def get_self(self):
        print(self)
    def ayu(self):
        self.c.ayu()#绑定引用时的实例化对象 self 和 c 使用ayu
        self.d.ayu()

''' print(c.get_self(b))
    print(c.get_self(c))
    print(c.get_self())
    print("===---===---===")
    print(b.get_self(c))
    print(b.get_self(b))
    print(b.get_self())
'''
print("将C()中实例化对象c获取属性y")
C().c.y = 10#将C()中实例化对象c获取属性y
C().d.y = 100
insec = C()
insec.ayu()

#使用  __dict__进行内省
print(insec.c.__dict__)

#通过类里面的方法设置对象里面的属性
print("\n #通过类里面的方法设置对象里面的属性")
class C:
    def set_x(self,v):
        self.x = v 
c = C()
print(c.__dict__)
c.set_x(201)
print(c.__dict__)
print(C().__dict__)#更改实例化对象属性不会改变类属性

#易错示范
print("\n#易错示范")
class B:
    x = 100
    def set_x(self,v):
        x = v
b = B()
b.set_x(199)
print(b.__dict__)
print(B().__dict__)
print(B().x)
print(b.x)

#小技巧
print("小技巧")
class dics:
    pass
dics.a = 100
dics.b = 250
dics.t = 'niumos'
print(f"a = {dics().a}, b = {dics().b}, t = {dics().t}")

#类里面定义的函数是函数 而 实例化对象的是方法
