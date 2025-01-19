#class 类
class Turtle:#习惯于大写第一个
    h = 1
    e = 2
    l = 4
    shell = True

    def crawl(self):#参数一定要加
        print("我很慢")

    def run(self):
        print("我可以很快")

    def eat(self):
        print("我会咬人（生气）")

    def sleep(self):
        print("Zzzzz...")

#可以把类赋值给对象 每个对象的数据不共享
'''可以 t.mouth = 1 创建对象里面新的数据'''

#封装  将数据赋值给对象
t = Turtle()
print(t.h)
t.mouth = 1
print(t.mouth)

class a:
    def b(biao):
        print(biao)

aa = a()#参数biao得到的值为实例对象aa本身
aa.b()
print(aa)
