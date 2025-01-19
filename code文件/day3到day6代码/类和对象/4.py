class C:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x+self.y
    def mul(self):
        return self.x*self.y

c = C(2,3)
print(c.add())
print(c.mul())

class D(C):
    def __init__(self,x,y,z):
        C.__init__(self,x,y)
        self.z = z
    def add(self):
        return C.add(self)+self.z
    def mul(self):
        return C.mul(self)+self.z
d = D(4,5,6)
print(d.add())
print(d.mul())
