#2.继承
'''子类 父类'''
class a:
    x = 222
    def hello(oo):
        print("dadsda")

class b(a):
    pass


b2 = b()
print(b2.x)
print(b().x)

#若类b内属性重新赋值，会进行覆盖
class b(a):
    x = 909
print(b().x)

#使用isinstance判断对象是否属于哪一个类
print(isinstance(b2,b))#重新改变了b导致 为False
print(isinstance(b2,a))

#检查是否为子类
print(issubclass(a,b))
print(issubclass(b,a))

#多重继承
class b():
    x =190
    xx = 1919

class c(a,b):
    pass

ce = c()
print(ce.x)#优先选择前面的
print(ce.xx)
'''print(ce.xxx)'''#会报错

#组合
class Cat():
    def say(x):
        print("喵喵喵~")

class Dog():
    def say(x):
        print("哟吼，我是一只修狗！")

class Garden:
    c = Cat()
    d = Dog()
    def say(self):
        self.t.say()
        self.t.say()

