#分支与循环  if  elif  else
x =1000
while x < 0 or x >100:
    a = input('请输入0到100分数')
    x = int(a)
#强制用户输入0--100的分
    if 0 <= x <= 100:
        break
#跳出
if x == 0:
    print('嗯。。。。。。。。。。。。')
elif 0 < x <=60:
    print('下次加油')
elif 60 < x <=80:
    print('bucuo')
elif 80 < x <= 99:
    print('很好了')
elif x == 100:
    print('作弊')
'''检验数据类型'''
print(type(a))

