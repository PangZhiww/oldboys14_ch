# print(1>1 or 3<4 or 4>5 and 2 >1 and 9>8 or 7<6)
# print(False or True or False or False)  # True
#
# print(not 2>1 and 3<4 or 4>5 and 2 >1 and 9>8 or 7<6)   #False
# print(False and True or False and True and True or False)
#
#
# print(8 or 3 and 4 or 2 and 0 or 9 and 7)
# print(8 or 4 or 0 or 7) # 8
#
# print(0 or 2 and 3 and 4 or 6 and 0 or 3)
# print(0 or 4 or 6 or 3) # 4
#
#
# print(6 or 2>1)     #   6
# print(6 or True)     #
#
# print(3 or 2>1)     #   3
# print(3 or 2>1)
#
# print(0 or 5>4)     #   True
# print(0 or 5>4)
#
# print(5<4 or 3)     #   3
# print(5<4 or 3)
#
# print(2>1 or 6)     #   True
# print(2>1 or 6)
#
# print(3 and 2>6)        #   False
# print(3 and 2>6)
#
# print(0 and 3>1)        #   0
# print(0 and 3>1)

# print(2>1 and 3)        #   3

# print(3>1 and 0)        #   True

# print(3>1 and 2 or 2<3 and 3 and 4 or 3>2)  # 2
# print(2 or 3>2)


# while True:
#     s = int(input("请输入一个数字："))
#     if s>66:
#         print("猜测结果大了")
#     if s<66:
#         print("猜测结果小了")
#     if s==66:
#         print("猜测结果正确")
#         break


# n = 66
# count = 1
# while count <= 3:
#     num = input("你猜一下")
#     if int(num) > n:
#         print("猜大了")
#     elif int(num) < n:
#         print("猜小了")
#     else:
#         print("猜对了！")
#         break
#     #   没猜对
#     print("你已经猜了%s次" %(count))
#     count = count + 1
# else:
#     print("你是个笨蛋！")


# count = 1
# while count <= 10:
#     print(count)
#     count = count + 1


# sum = 0
# count = 1
# while count <= 100:
# 	print(count)
# 	sum = sum + count
# 	count = count + 1
# print(sum)


# count = 1
# while count <= 100:
# 	if count % 2 != 0:
# 		print(count)
# 	count = count + 1

# count = 1
# while count <= 100:
# 	if count % 2 != 1:
# 		print(count)
# 	count = count + 1


# count = 1
# while count <= 10:
#     if count != 7:
#         print(count)
#     count = count + 1

# count = 1
# while count <= 10:
#     if count == 7:
#         # pass
#         # count = 8
#         count = count + 1
#         continue
#     print(count)
#     count = count + 1


# sum = 0
# count = 1
# while count < 100:
#     if count % 2 == 0:  # 偶数
#         sum = sum - count
#     else:   # 奇数
#         sum = sum + count
#     count = count + 1
# print(sum)


#   用户登录：用户名：alex，密码：sb
# username = input("请输入你的用户名：")
# password = input("请输入你的明码：")
# if username == 'alex' and password == 'sb':
#     print("登陆成功")
# else:
#     print("登录失败")

# count = 1
# while count <= 3:
#     username = input("请输入你的用户名：")
#     password = input("请输入你的明码：")
#     if username == 'alex' and password == 'sb':
#         print("登陆成功")
#         break
#     else:
#         print("登录失败")
#
#     print("还剩余%d次机会" % (3 - count))
#     count = count + 1
# else:
#     print("蠢！")


# ad = input("请输入你的广告标语：")
# if '最' in ad or '国家级' in ad or '第一' in ad or '稀缺' in ad:
#     print("不合法！")
# else:
#     print("合法！")