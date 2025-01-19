#类和对象 多态——同一个运算符，函数....在不同场景下有不同的使用

#如:
print(3+5)
print("fishc"+".com")

print(len("1123"))#多态
print(len([1,1,1,1,1]))


'''重写实现类继承多态'''
class Shape:#形状
    def __init__(self,name):
        self.name = name

    def area(self):
        pass

class Square(Shape):#正方形
    def __init__(self,length):
        super().__init__("正方形")
        self.length = length
    def area(self):
        return self.length**2

class Circle(Shape):
    def __init__(self,length):
        super().__init__("圆形")
        self.length = length

    def area(self):
        return self.length**2*3.14/4

a = Square(5)
b = Circle(6)
def aa(x):
    print(x.area())
    
aa(a)
aa(b)

    
