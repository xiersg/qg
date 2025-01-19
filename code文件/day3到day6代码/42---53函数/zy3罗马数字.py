x = dict(zip(['I','V','X','L','C','D','M'],[1,5,10,50,100,500,1000]))
#创造一个字典，用来转化
y = ('I','V','X','L','C','D','M')
#创造一个列表用来索引，判断是加还是减

def ml(num):
    summ = 0
    for i in range(len(num)):
        if (not(num[i] in y)): #检查防止字符不是罗马数字导致错误
            print('请输入罗马数字')
            break
        a = x[num[i]]
        if i != len(num)-1 and num[i+1] in y and y.index(num[i])<y.index(num[i+1]):  
            a = -a    #用来实现罗马数字的特殊法则
        summ += a
        print(summ,a)

    print("结果为{}".format(summ))
        
x2 = dict(zip([1,4,5,9,10,40,50,90,100,400,500,900,1000],['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']))
y2 = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
def ml2(num2):
    num_lm = ''
    for i in y2[::-1]:
        a = num2//i
        num_lm = ''.join((num_lm,x2[i]*a))
        num2 -= a*i
    print(num_lm)
