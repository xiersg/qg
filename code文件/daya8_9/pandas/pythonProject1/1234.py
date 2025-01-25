import random

def prize(l = 1000,r = 1500):
    temp = list(map(int,random.sample(range(l,r),k = 500)))
    temp = temp[random.randint(0,1500)//3]
    if temp not in nums2:
        if temp not in nums1:
            nums1.append(temp)
            return 0
        else:
            nums2.append(temp)
            return 0
    else:
        print(f"result = {temp}")
        return temp

nums1,nums2 = [],[]
count = 0
while(1):
    if (prize() != 0):
        break
    print(f"nums1 = {nums1}")
    print(f"nums2 = {nums2}")
    count+=1
print(f"count = {count}")
print(len(nums1))