import random
# 随机: 在某个范围你取到每一个值的概率是相同的
# 随机小数
# 无限循环小数, 包含在float里
# 无限不循环小数, 不包含在float里

# print(random.random())  # 0-1之内的随机小数
# print(random.uniform(1,5))  # 1-5之内的随机小数    任意范围内的随机小数


# 随机整数  *****
# print(random.randint(1,2))  # [1,2]包含2在内的范围内随机去整数   闭区间
# print(random.randrange(1,2))    # [1,2)不包含2在内的范围内随机取整数   左闭右开
# print(random.randrange(1,10,2)) # [1,10)不包含10在内的范围内随机取奇数   左闭右开


# 随机抽取
    # 随机抽取多个值
# lst = [1,2,3,"aaa",("wahaha","qqxing")]
# ret = random.choice(lst)
# print(ret)

    # 随机抽取多个值
# ret = random.sample(lst,2)
# print(ret)


# 打乱顺序  在原有列表的基础上打乱顺序
# lst = [1,2,3,"aaa",("wahaha","qqxing")]
# random.shuffle(lst)
# print(lst)


# 永远不要创建一个和你知道的模块同名的文件名



# 生成随机验证码
# 4位数字
# 基础版本
# import random
# code = ""
# for i in range(6):
#     num = random.randint(0,9)
#     code = code + str(num)
# print(code)


# 函数版本
# def read_code(n=4):
#     code = ""
#     for i in range(n):
#         num = random.randint(0,9)
#         code = code + str(num)
#     return code
# print(read_code(6))



# 6位 数字+字幕
# print(chr(97))
# print(chr(122))

# 基础版
# import random
# code = ""
# for i in range(6):
#     rand_num = str(random.randint(0,9))
#     rand_alph = chr(random.randint(97,122))     # chr()直接生成字符串
#     rand_alph_upper = chr(random.randint(65,90))
#     atom_code = random.choice([rand_num,rand_alph,rand_alph_upper])
#     code = code + atom_code
# print(code)

# 函数版
# 简单的
import random
# def rand_code(n=6):
#     code = ""
#     for i in range(n):
#         rand_num = str(random.randint(0,9))
#         rand_alph = chr(random.randint(97,122))     # chr()直接生成字符串
#         rand_alph_upper = chr(random.randint(65,90))
#         atom_code = random.choice([rand_num,rand_alph,rand_alph_upper])
#         code = code + atom_code
#     return code
# print(rand_code())


#数字／数字＋字母
import random
def rand_code(n=6,alph_flag=True):
    code = ""
    for i in range(n):
        rand_num = str(random.randint(0,9))
        if alph_flag:
            rand_alph = chr(random.randint(97,122))     # chr()直接生成字符串
            rand_alph_upper = chr(random.randint(65,90))
            rand_num = random.choice([rand_num,rand_alph,rand_alph_upper])
        code = code + rand_num
    return code
ret = rand_code(n=4,alph_flag=False)    # alph_flag=False 只生成数字
print(ret)