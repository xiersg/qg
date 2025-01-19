# 题目要求：
# 请在此处补充装饰器 type_check() 的代码
def type_check(types):
    def type_csno(func):
        def call_func(x):
            if types == 'str':
                if type(x) == type('str'):
                    x = func(x)
                else:
                    return "参数类型错误"
            if types == 'int':
                if type(x) == type(123):
                    x = func(x)
                else:
                    return "参数类型错误"
            return x
        return call_func       
    return type_csno


print("<<<--- 测试整数 --->>>")

@type_check(types = "int")
def double(x):
    return x * 2

print(double(2))      # 这里打印结果应该是 4
print(double("2"))    # 这里打印结果应该是 “参数类型错误”


print("\n<<<--- 测试字符串 --->>>")

@type_check(types = "str")
def upper(s):
    return s.upper()

print(upper('I love FishC.'))   # 这里打印结果应该是 I LOVE FISHC
print(upper(250))               # 这里打印结果应该是 “参数类型错误”
