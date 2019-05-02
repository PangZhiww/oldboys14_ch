# 布尔类型转换
# s = 128
# i = bool(s)
# print(i)
# print(type(i))

# ss = str(s)
# print(ss)
# print(type(ss))

# s = "你好，我很好！"
# i = bool(s)
# print(i)
# print(type(i))

# s = "123"
# i = int(s)
# print(i)
# print(type(i))

# b = True
# i = int(b)
# print(i)
# print(type(i))

# a = False
# b = int(a)
# print(b)
# print(type(b))

# a = 0
# b = bool(a)
# print(b)
# print(type(b))

# a = 12
# b = bool(a)
# print(b)
# print(type(b))

# s = "你好！"
# if s:
#     print("哈哈哈")
# else:
#     print("hehe")

# s = ""
# if s:
#     print("haha")
# else:
#     print("hehe")

# a = None
# if a:
#     print("haha")
# else:
#     print("hehe")


# 字符串
# s = "今天是个好日子，天气特别好"
#[
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print(s[5])
# print(s[6])
# print(s[7])
# print(s[8])
# print(s[9])
# print(s[10])
# print(s[11])
# print(s[12])
#
# print(s[-1])
# print(s[-0])
# print(s[-2])
# print(s[-3])
# print(s[-4])
#]
# s1 = s[4:6]
# print(s1)
# s2 = s[3:5] + s[8:11]
# print(s2)
# s3 = s[5:]
# print(s3)
# s4 = s[:11]
# print(s4)
# s5 = s[:]
# print(s5)

# s6 = s[-8:-3]
# print(s6)
# s7 = s[-5:]
# print(s7)
# s8 = s[:-5]
# print(s8)

# s1 = s[3:9:2]
# print(s1)
# s2 = s[5:12:3]
# print(s2)
# s3 = s[::5]
# print(s3)
# s4 = s[10:1:-3]
# print(s4)
# s5 = s[5::2]
# s5 = s[5::-2]
# s5 = s[10::-3]
# print(s5)
# s6 = s[-2:-8:-3]
# print(s6)


# 字符串操作
# s = "alex and taibai bubai and wusir"
# s1 = s.capitalize()
# print(s1)
# s2 = s.upper()
# print(s2)
# s3 = s2.lower()
# print(s3)

# while True:
#     content = input("请输入：")
#     if content.upper() == "Q":
#             print("haha")
#             break
#     print("hehe")

# verify_code = "abDe"
# user_verify_code = input("请输入验证码：")
# if verify_code.upper() == user_verify_code.upper():
#     print("验证成功")
# else:
#     print("验证失败，请重新输入！")

# while True:
#     content = input("请输入：")
#     if content.lower() == "q":
#         print("haha")
#         break
#     print("hehe")

# s = "jobAAdhjADFisaSDadfaASdfDdo"
# s1 = s.swapcase()
# print(s1)

# s = "jiodf jhfdaio fsd建瓯市东方红bjia kaih"
# print(s.title())

# s = "马化腾"
# s1 = s.center(9,'*')
# print(s1)

# s = " 我是alex "
# s1 = s.strip()
# print(s1)
# s2 = s.lstrip()
# print(s2)
# s3 = s.rstrip()
# print(s3)

# username = input("用户名：").strip()
# password = input("密码：").strip()
# if username == "alex" and password == "123":
#     print("haha")
# else:
#     print("hehe")

# username = input("请输入：").lower().strip()
# password = input("密码:").lower().strip()
# if username == "alex" and password == "123":
#     print("输入正确!")
# else:
#     print("登录失败")

# s = "dsd阿好久哦天平山dsd"
# s1 = s.strip("dsd")
# print(s1)

# s = "Alex wusir alex sb taibai"
# s1 = s.lower().replace("alex", "小学")
# print(s1)

# s = "Alex upper lower replace strip capitalize"
# s1 = s.replace("replace","strip")
# print(s1)

# s = "alex wuse taibai bubai upper"
# s1 = s.split(" ")
# print(s1)

# s = "123*456*789*741*852*963"
# s1 = s.split("*")
# print(s1)

# s = "你好,我是{}警官,是{}警察,我在找{},请问你有见到她吗?".format("人民","你们","Alex")
# print(s)

# s = "今天的天气{},适合{},我要给{}打电话".format("很好","出去散步","Alex")
# print(s)

# s = "请问你是{name}吗?你的ID是{number}吗?今年{age}岁了吗?".format(name="姓名",age="年龄",number="身份证号码")
# print(s)

# s = "请问你今年{age}大了,我是来自{dress}的{name},很高兴认识你".format(age="18",dress="canada",name="Alex")
# s1 = s.upper().split(",")
# print(s1)

# s = "汪峰的老婆不爱Alex".upper()
# s1 = s.endswith("ALEX")
# print(s1)

# s = "汪峰的老婆是国际章"
# s1 = s.replace("国际章","Alex")
# s2 = s1.lower()
# s3 = s2.endswith("alex")
# print(s3)

# s = "汪峰的老婆爱汪峰"
# s1 = s.startswith("汪峰")
# print(s1)

# s = "汪峰的老婆爱Alex"
# s1 = s.upper()
# s2 = s1.replace("ALEX","汪峰")
# s3 = s2.count("汪峰")
# print(s3)

# s = "汪峰的老婆爱汪峰"
# s1 = s.find("汪峰",5)
# s2 = s.find("国际章")
# print(s1)
# print(s2)

# s = "汪峰的老婆是国际章"
# s1 = s.index("汪峰",4)
# print(s1)

# s = "你今天喝酒了吗?"
# s1 = len(s)
# print(s1)

# s = "小学老师,你好漂亮啊!"
# print(len(s))
# count = 0
# while count <= len(s):
#     print(s[count])
#     count = count +1

# s = "fgkjfndbdijfhbgfioacfvkljbdsafjiopsdbfjvhsdbgojfgvsdhbgpiojgvzxc"
# print(len(s))
# count = 0
# while count < len(s):
#     print(s[count])
#     count = count + 1

# s = "我们是来自五湖四海的人"
# print(len(s))
# count = 0
# while count < len(s):
#     print(s[count])
#     count = count + 1

# b = "在我这里 "
# for c in b:
#     print(c)


# 作业
# name = "aleX leNb  "
# print(name.strip())
# print(name.strip("al"))
# print(name.strip("Nb"))
# print(name.strip("ab"))
# print(name.startswith("al"))
# print(name.endswith("Nb"))
# print(name.replace("l","p"))
# 将name变量对应的的值中的第一个"l"替换为"p"
# print(name.replace("l","p",1,5))?
# print(name.split("l"))
# 将name变量对应的值根据第一个"l"分割
# print(name.split("l"))?
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.find("l"))
# print(name.find("l",0,4))
# print(name.index("N"))
# print(name.find(N))
# print(name.find("X le"))
# print(len(name))
# print(name[2])
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[7])
# print(name[8])


# e1 = name.find("e", 0,5)
# print(e1)
# e2 = name.find("e", 5)
# print(e2)

# count = 0
# while count < len(name):
#     if name[count] == 'e':
#         print(count)
#     count = count + 1



# s = "123a4b5c"
# s1 = s[:3]
# print(s1.split("a"))

# s2 = s[3:6]
# print(s2.split("5"))

# s3 = s[:5]
# print(s3.split("b"))

# print(s[0:7:2])
# print(s[1:7:2])
# print(s[7])
# print(s[-3:-8:-2])


# s = "asdfer"
# count = 0
# while count < len(s):
#     print(s[count])
#     count = count + 1

# for c in s:
#     print(c)

# for c in s:
#     print(c + "sb")


# s = "321"
# for c in s:
#     print("倒计时"+c+"秒")
#     print("出发!")
# s1 = "倒计时{}秒,倒计时{}秒,倒计时{}秒,出发!".format("3","2","1")
# print(s1)
# for c in s:
#     print("倒计时%s" % c)
# else:
#     print("出发!")


# content = input("请输入内容:")
# lst = content.split("+")
# print(lst)
# s1 = lst[0]
# s2 = lst[1]
# a1 = int(s1)
# a2 = int(s2)
# print(a1 + a2)


# content = input("请输入内容:")
# lst = content.split("+")
# print(lst)
# s1 = lst[0]
# s2 = lst[1]
# s3 = lst[2]
# s4 = lst[3]
# s5 = lst[4]
# a1 = int(s1)
# a2 = int(s2)
# a3 = int(s3)
# a4 = int(s4)
# a5 = int(s5)
# print(a1 +a2+a3+a4+a5)


# content = input("请输入内容:")
# count = 0
# for c in content:
#     if c.isdigit():
#         count = count + 1
# print(count)


# while True:
#     count = input("请输入A,B或C:").upper().strip()
#     if count == "A":
#         jiaotong = input("请选择公交车或者步行:")
#         if jiaotong == "公交车":
#             print("您还需要10分钟到家")
#             break
#         elif jiaotong == "步行":
#             print("你还需要20分钟到家")
#             break
#         else:
#             print("我也不知道怎么办!")
#     elif count == "B":
#         print("走小路回家")
#         break
#     elif count == "C":
#         play =input("请选择游戏厅或者网吧:")
#         if play == "游戏厅":
#             print("一个半小时到家,爸爸在家,拿棍等你")
#             continue
#         elif play == "网吧":
#             print("两个小时到家,妈妈已做好战斗准备")
#             continue
#         else:
#             print("我就是喜欢浪!")
#     else:
#         print("你是不是傻!")


# count = 1
# sum = 0
# while count < 100:
#     if count == 88:
#         count = count + 1
#         continue
#
#     if count %2 == 0:
#         sum = sum - count
#     else:
#         sum = sum + count
#
#     count = count + 1
# print(sum)


# s = "上海自来水来自海上"
# s = "明天到操场操到天明"
# s1 = s[::-1]
# if s == s1:
#     print("回文")
# else:
#     print("不是回文")


# coutent = input("请输入一个字符串：")
# digit_num = 0
# upper_c_num = 0
# lower_c_num = 0
# other = 0
#
# for c in coutent:
#     if c.isdigit():
#         digit_num = digit_num + 1
#     elif c.isupper():
#         upper_c_num = upper_c_num + 1
#     elif c.islower():
#         lower_c_num = lower_c_num + 1
#     else:
#         other = other + 1
#
# print(digit_num)
# print(upper_c_num)
# print(lower_c_num)
# print(other)


# name = input("请输入你的名字:")
# address = input("请输入你的地点:")
# something = input("请输入你要做的事情:")
# s = "敬爱可亲的{name},最喜欢在{address}地方干{something}".format(name=name,address=address,something=something)
# print(s)


# s = "欧阳娜娜"
# ss = ""
# for c in s:
#     ss = ss + c
#     print(ss)