#截取字符串

#lstrip() 去除左侧空格 同理 rstrip() 去除右侧空格
x = "   没有留白   "
print(x)
print(x.lstrip())
#strip() 去除左右的空格
#在()中加入指定剔除目标会一直剔除匹配目标直到不匹配
x = 'niumoniumooo.qq.comm'
y = x.strip('niumo')
print(y)

#剔除指定目标 removeprefix() removesuffix()
x = "www.在座的各位，都是牛魔！！.com"
#剔除前缀 只能在最前 有空格都不行
print(x.removeprefix("www."))
#剔除后缀 同上
print(x.removesuffix(".com"))


#拆分 和 拼接

#partition() rpartition()
x = "www.ilovexier.com"
#partition从左到右进行分割，分割结果储存至三元元组
y = x.partition(".")
print(y)
#rpartition从右到左进行分割，同上
y = x.rpartition(".")
print(y)

#split('分割标识',分割次数) rsplit  其中分割次数为-1时全部分割
#同上，一个从左到右，一个从右到左
x = "www.kami.xier.com"
print(x.split(".",-1))
#splitlines() 是直接将换行进行分割  \n \r \r\n 三种换行符
#括号内参数为包不包含换行符
x = "www\nkami\nxier\ncom"
print(x.splitlines())

#join 拼接
print('.'.join(('f','ish','c')))
y = ('FishC')
print(type(y))
j = "".join([y*2])
print(j)
