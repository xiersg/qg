#字符串3

#判断 

#startswith('a'[,start[,end]])判断指定子字符串是否在字符串开头,空格也算
x = '我是小甲鱼'
d = x.startswith(' ')
print(d)
#endswith('a',[start[,end]]) 判断是否在末尾 以下 0，5为开始和结束位置
d2 = x.endswith('鱼',0,5)
print(d2)
#其中搜索的字符串可以以元组的方式输入，只需要一个对，就输出True
#不能以列表的方式输入
d3 = x.startswith(('我','你','她'))
if d3 == True:
    print('总有人喜欢python')
print()

#istitle() 判断是否全部为大写开头
x = 'I love FishC'
d = x.istitle()
print(d)
x2 = x.title()
print(x2)
d2 = x2.istitle()
print(d2)
print()

#isupper 判断是否全为大写
#从左往右依次进行
print(x.upper().isupper())
print()

#剩下的以此类推 islo

#isalpha 检测是否全部为字母
# isalpha() 方法判断的 “字母” 是 Unicode 编码中定义的字母，不止是 26 个英文字母哈^o^()
print(x.isalpha())
#因为空格不是字母

#isspace 检测是否为空白字符串
print(' '.isspace())
print(' '.isspace())
print('\n'.isspace())
print('\t'.isspace())
print()

#isprintable 判断是否可打印
'''
在Python中，‌不可打印字符主要指的是那些无法直接显示或打印的字符，‌
这些字符通常用于控制文本格式或执行特定功能。‌
具体来说，‌不可打印字符包括：‌

控制字符：‌这些字符用于控制文本的显示或处理，‌而不是用于显示给用户看。‌例如，‌\c 匹配由 x 指明的控制字符，‌其中 x 的值必须是 A-Z 或 a-z 的大小写字符。‌具体的控制字符包括：‌
\f 匹配一个换页符。‌
\n 匹配一个换行符。‌
\r 匹配一个回车符。‌
\t 匹配一个制表符。‌
 这       \v 匹配一个垂直制表符。‌
 三 以     \s 匹配任何空白字符，‌等效于 [\r\n\r\t\v]。‌
 可         \S 匹配任何非空白字符。‌'''
print('\n'.isprintable())
print()



#判断数字
#isdecimal isdigit isnumeric
for i in ['123','ⅠⅡⅢ','一二三','①②③','2²']:
    print(i.isdecimal())
    print(i.isdigit())
    print(i.isnumeric())
    print()
#isalnum 集大成者，只要前三和isalpha有一为True则结果为True 用于检查是否只有英文或者数字
print('djdj2334'.isalnum())
print('-133dkf'.isalnum())
print()

#isidentifier 判断字符串是否为一个合法的标识符
y = 'I am a good dog'
x = y.isidentifier()
print(x)
y = y.replace(' ','_')
x = y.isidentifier()
print(x)
print()

#判断是否为保留标识符
import keyword
z = input('输入')
x = keyword.iskeyword (z)
print(x)


