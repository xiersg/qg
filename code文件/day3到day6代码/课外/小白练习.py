print("1<=a,b,c<=10**9*2")
a = int(input("a请输入数字："))
b = int(input("b请输入数字："))
c = int(input("c请输入数字："))

x = [a,b,c]
for i in range(0,3):
    if abs(x[i-1]-x[i-2])< x[i] * 2 < a + b + c - x[i]:
        print("yes")
        break
else:
    print("No")
