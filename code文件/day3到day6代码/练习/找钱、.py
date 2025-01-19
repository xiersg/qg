n = int(input())
#暴力枚举
te = 0
for i in range(n//10 + 1):
    for j in range((n-10*i)//5+1):
        if (10*i+5*j)<= n:
            print(10*i+5*j)
            te+=1
print(te)

#背包
dp = [0 for _ in range(n+1)]
dp[0] = 1
v = [1,5,10]
for i in range(3):
    for j in range(1,n+1):
        if j-v[i]>=0:
            dp[j] += dp[j-v[i]]
print(dp,'\n',dp[-1])
