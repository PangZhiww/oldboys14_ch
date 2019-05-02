# 计数

# count = 1
# while count <= 8:
#     count = count + 1
#     print("你是alex么？")
#     print("你全家都是太白")
#


#让用户尽情的喷，输入q退出
# while True:
#     s = input("请开始喷：")
#     if s == 'q':
#         break   #   停止当前循环
#     # 过滤掉马化腾
#     if "马化腾" in s:   # 在XXX中出现了XX
#         print("你输入的内容不合法！")
#         continue        # 停止当前本次循环，继续执行下一次循环
#     print("喷的内容是：" + s)




# count = 1
# #   准备一个变量
# sum = 0
# while count <= 100:
#     print(count)
#     #   累加到sum中
#     sum = sum+ count        #   把sum中的值（之前的运算结果）和当前数的数相加
#     count = count + 1
# print(sum)


#   输出1-100所有的奇数
count = 1
while count <= 100:
    if count % 2 != 0:
        print(count)
    count = count + 1


