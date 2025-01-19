n = [1,2,3,4,5,6,7,8,9]

for a in n[0:3:]:
    for b in n[a*2-1:6:]:
        for c in n[a*3-1::]:
            n = [1,2,3,4,5,6,7,8,9]
            n[a-1] = 0
            n[b-1] = 0
            n[c-1] = 0
                           
            for a2 in n:
                n1 = n
                if a2 == 0: 
                    continue
                at = a*10 + a2
                n[a2-1] = 0

                
                for b2 in n:
                    if b2 == 0:
                        continue
                    bt = b*10 + b2
                    n[b2-1] = 0


                    for c2 in n:
                        if c2 == 0:
                            continue
                        ct = c*10 + c2
                        n[c2-1] = 0

                        n2 = []
                        print(at,bt,ct)
                        if ct >= at*3 and bt >= at*2:
                            for i in n:
                                if i != 0:
                                    n2.append(i)
                                    
                            for i in range(3):
                                n3 = n2
                                at = at*10 + n3.pop(i)
                                

                                for i2 in range(2):
                                    b3 = bt*10 + n3.pop(i2)
                                    c3 = ct*10 + n3[0]
                                    
                                    print(at,bt,ct)

                                    if ct == at*3 and bt == at*2:
                                        print(at,bt,ct)

                            
                    
