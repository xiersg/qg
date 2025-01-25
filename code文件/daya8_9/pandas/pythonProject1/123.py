import random
import time

#list(map(int,random.choices(range(0,n),k = x)))

def prize(temp):
    if temp not in nums2:
        if temp not in nums1:
            nums1.append(temp)
            return 0
        else:
            nums1.remove(temp)
            nums2.append(temp)
            return 0
    else:
        print(f"result = {temp}")
        return temp

nums1 = []
nums2 = []
count = 0
while(1):
    print(f"nums1 = {nums1}")
    print(f"nums2 = {nums2}")
    count += 1
    k2 = random.randint(1,100)
    temp = random.choices(range(1000,1501),k = k2+1)
    if prize(temp[random.randint(1,k2)]):
        break
print(f"count = {count}")
