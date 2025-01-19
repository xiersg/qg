#汽车租赁系统

class Caroperation:
    def __init__(self):#初始化
        Jcar,Hcar,Pcar,Scar = [],[],[],[]
        self.car = [Jcar,Hcar,Pcar,Scar]
        self.a = ["品牌：","型号：","租金：","补贴：","保险","损耗"]
        self.b = ["经济车辆(享有补贴)",'豪华车(需要额外购买保险)','跑车(需增加损耗费用)',"SUV(租赁超过7天，可享额外7折上优惠)"]
        
    def register(self,x,n):#录入汽车
        for _ in range(n):
            stats = []
            if x == 1 or x == 4:
                for i in [0,1,2,3]:
                    stats.append(input(self.a[i]))
            if x == 2:
                for i in [0,1,2,4]:
                    stats.append(input(self.a[i]))
            if x == 3:
                for i in [0,1,2,5]:
                    stats.append(input(self.a[i]))
            self.car[x-1].append(stats)
            print("录入成功！\n")

    def get_stock(self):#获取库存
        for i in range(len(self.car)):
            print(f"{i}.{self.b[i]},共有{len(self.car[i])}辆")#读表
            for j in range(len(self.car[i])):
                print(f"编号：{(i+1)*10000+j}",end = ' ')
                for k in range(4):
                    print(f"{self.a[k]}{self.car[i][j][k]}",end = ' ')
                print()
            print()

    def calc_rent(self,zu,t,e,x):
        if x == 3 and t>=7:
            return (zu+e)*t*0.7
        else:
            return (zu+e)*t
        
        
    def rent_car(self):#租车
        self.get_stock()
        n = int(input("请输入想要租赁的车辆编号："))
        time = int(input("请输入想要租赁的天数"))#(self.car[n//10000-1][n%10000-1][2]-self.car[n//10000-1][n%10000-1][3])*time
        print(f"租赁{time}天,共花费{self.calc_rent(int(self.car[n//10000-1][n%10000][2]) , time , 0-int(self.car[n//10000-1][n%10000][3]) , int(n//10000-1))}")
        self.car[n//10000-1].pop(n%10000)
        
    def return_car(self):#还车
        pass

    def operate(self):#程序入口
        m = int(input("欢迎使用希儿的汽车租赁系统！\n\n1.录入汽车  2.租车服务  3.还车服务  4.退出程序"))
        if m == 4:
            return 0
        elif m == 1 or m == 3:
            x = int(input("1.经济车型;2.豪华车;3.跑车;4.SUV:"))
            n = int(input("请输入录入数量"))
            self.register(x,n)
        elif m == 2:
            self.rent_car()

c = Caroperation()
while(1):
    n = c.operate()
    if n == 0:
        break



            

