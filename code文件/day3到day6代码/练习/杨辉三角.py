x = [1]
y = [1,1]
z = [1,1]
n = int(input("次数"))
print(f"{" "*n}{x}{" "*n}")
print(f"{" "*(n-1)}{y}{" "*(n-1)}")
for i in range(2,n):
    z = [1,1]
    for i2 in range(len(y) - 1):
        a = y[i2] + y[i2 + 1]
        z.insert(-1,a)
    y = z
    print(f"{" "*(n-i)}{z}{" "*(n-i)}")
