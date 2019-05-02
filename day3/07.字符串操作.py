s = "alex and wusir and taibai"
s1 = s.capitalize()     # 首字母大写
print(s)    # 原字符串不变
print(s1)

# s = "Alex is not a Good Man"
# print(s.upper())    # 全部大写
# print(s.lower())    # 全部小写

# 在程序需要判断不区分大小写的时候，肯定能用
# while True:
#     content = input("请喷：")
#     # if content == 'q' or content == 'Q':
#     if content.upper() == 'Q':
#         break
#     print("你喷了：",content)

# s = "hDFAjidfFGsgsGHhjofS"
# print(s.swapcase())   # 大小写转换

# s = "afa马化腾ew fg fsgd saf"
# print(s.title())     # 每个被特殊字符隔开的字⺟母⾸首字⺟母⼤大写

# s = "麻花藤"
# print(s.center(8,'*'))    # # 拉⻓长成8, 把原字符串串放中间.其余位置补*

# username = input("用户名：").strip()    # 去掉左右两端的空格
# password = input("密码：").strip()     # 去掉空格
# if username == "alex" and password == "123":
#     print("登陆成功")
# else:
#     print("登录失败")

# username = input("用户名：").strip()
# password = input("密码：").strip()
# if username == 'alex' and password == '123':
#     print("登陆成功")
# else:
#     print("登录失败")

# s = "aaaaaabbabaaaa"
# print(s.strip("a"))     # strip去掉的是左右两端的内容，中间的不管

# s = "alex wusir alex sb taibai"
# s1 = s.replace("alex","小雪")
# print(s1)   # 去掉上述字符串中的所有空格
# s2 = s.replace(" ", "")
# print(s2)
# s3 = s.replace("alex", "sb", 1)
# print(s3)

# s = "alex_wuse_taibai_bubai"
# lst = s.split("_")      # 刀是 _ 切完的东西是列表，列表装的是字符串
# lst = s.split("_taibai_")
# lst = s.split("_taibai_bubai")      #   空字符
# print(lst)

# s = "我叫{}，我今年{}岁了，我喜欢{}".format("sylar",18,"周杰伦的老婆")
# s1 = "我叫{1}，我今年{2}岁了，我喜欢{0}".format("sylar",18,"周杰伦的老婆")    # 可以指定位置15136*1682
# s2 = "我叫{name}，我今年{age}岁了，我喜欢{some}".format(name="sylar",age=18,some="周杰伦的老婆")
# print(s2)


# 15136111682


# s = "汪峰的老婆不爱汪峰"
# print(s.startswith("汪峰"))       # 判断字符串是否以XXX开头
# print(s.endswith("爱妃"))     # 判断字符串时候以XXX结尾
# print(s.count("国际章"))       # 计算XXX在字符串中出现的次数
# print(s.find("汪峰"))
# print(s.find("汪峰",3))
# print(s.find("国际章"))      # 计算XXX字符串在原字符串中出现的位置，如果没有返回 -1
# print(s.index("国际章"))       # index中的内容如果不存在，直接报错

# s = "abcd123"
# print(s.isdigit())      # 判断字符串是否由数字组成
# print(s.isalpha())      # 判断字符串是否由字母组成
# print(s.isalnum())      # 判断字符串是否由字符和数字组成

# s =  "二千123万萬"
# print(s.isnumeric())

# s = "你今天喝酒了吗？"
# i = len(s)  # print() input() len() python的内置函数
# print(i)

# i = s.__len__()    # 也可以求长度  len()函数执行的时候实际执行的就是它
# print(i)

# s = "小雪老师，你好漂亮"
# print(len(s))   # 长度是：9     索引是：8
# 1.使用while循环来进行遍历
# count = 0
# while count < len(s):
#     print(s[count])
#     count = count + 1

# 2.用for循环来遍历字符串
# 优势：简单
# 劣势：没有索引
# for c in s:
    # print(c)
#
# 语法：
    # for 变量 in 可迭代对象：
        # 循环体