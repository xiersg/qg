# Mixin

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say(self):
        print(self)
        print(f"我叫{self.name},今年{self.age}岁")

class flyMixin():
    def flye(self):
        print("我还会飞")

class Pig(Animal,flyMixin):
    def special(self):
        print("我的技能是__---__")

p = Pig("大肠",10)
p.say()
p.special()
p.flye()

#神奇的顺序
class Displayer:
    def displayer(self,messge):
        print(messge)

class LoggerMixin:
    def displayer(self,message):
        super().displayer(message)
        self.log(message)

    def log(self,message,filename = 'logfilr.txt'):
        with open(filename,'a') as f:
            f.write(message)

class MySub(LoggerMixin,Displayer):
    def log(self,message):
        super().log(message,filename = "subclass_xier.txt")

subclass = MySub()
subclass.displayer("This is a test")
