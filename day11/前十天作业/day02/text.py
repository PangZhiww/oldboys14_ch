# print(1>1 or 3<4 or 4>5 and 2>1 and 9>8 or 7<6)
# print(not 2>1 and 3<4 or 4>5 and 2>1 and 9>8 or 7<6)
#
# print(8 or 3 and 4 or 2 and 0 or 9 and 7)
# print(0 or 2 and 3 and 4 or 6 and 0 or 3)

# print(6 or 2>1)
# print(3 or 2>1)
# print(0 or 5<4)
# print(5<4 or 3)
# print(2>1 or 6)
# print(3 and 2>1)
# print(0 and 3>1)
# print(2>1 and 3)
# print(3>1 and 0)
# print(3>1 and 2 or 2<3 and 3 and 4 or 3>2)



# while 1:
#     s = int(input("请输入你心目中想的数字:"))
#     if s > 66:
#         print("你想的结果大了")
#     elif s < 66:
#         print("你猜的结果小了")
#     else:
#         print("结果正确")
#         break



# count = 1
# while count <= 3:
#     num = input("你猜一下:")
#     if int(num) > 66:
#         print("猜大了")
#     elif int(num) < 66:
#         print("猜小了")
#     else:
#         print("猜对了!")
#         break
#     print("你已经猜了%d次了" % count)
#     count = count + 1
# else:
#     print("你是个笨蛋!")


# count = 1
# while count <= 10:
#     print(count)
#     count = count + 1


# sum = 0
# count = 1
# while count <= 100:
#     sum = sum + count
#     count = count + 1
#
# print(sum)



# count = 1
# while count <= 100:
#     if count % 2 != 0:
#         print(count)
#     count = count + 1


# count = 1
# while count <= 100:
#     if count % 2 == 0:
#         print(count)
#     count = count + 1


# count = 1
# sum = 0
# while count < 100:
#     if count % 2 == 0:
#         sum = sum - count
#     if count % 2 != 0:
#         sum = sum + count
#
#     count = count + 1
# print(sum)



# count = 1
# while count <= 3:
#     s = input("请你输入密码:")
#     print("你是剩余%s次机会" %  (3 - count))
#     count = count + 1


# s = input("请输入:")
# if '最' in s or '第一' in s or "稀缺" in s or "国家级" in s:
#     print("不合法")
# else:
#     print("合法")