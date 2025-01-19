for a in range(123,333,1):
    x = a
    b = a*2
    c = a*3

    n = []
    for i in range(3):
        e = a%10
        a = (a - e)/10

        f = b%10
        b = (b - f)/10

        g = c%10
        c = (c - g)/10

        n.append(int(e))
        n.append(int(f))
        n.append(int(g))
        n.sort()

    for i in range(8):
        if n[i] == n[i+1] or n[i] == 0 or n[i+1] == 0:
            break
        
    else:
        print(x,x*2,x*3)
