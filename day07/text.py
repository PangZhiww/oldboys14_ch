#   第一题
# while 1:
#     n = input("请输入一个三位数:")
#     s = int(n[0]) ** 3 + int(n[1]) ** 3 + int(n[2]) ** 3
#     if int(n) == s:
#         continue
#         print("是水仙花")
#     else:
#         print("不是水仙花")


#第二题
# a = 10
# b = 20

# lst = [22,33,8,44,1,5,9,6]
# for i in range(7):
#     i = 0
#     while i < len(lst) - 1:
#         if lst[i] > lst[i+1]:
#             lst[i],lst[i+1] = lst[i+1] , lst[i]
#         i = i + 1
# print(lst)
# a,b = b,a
# print(a,b)

#c的思想
# x = a
# a = b
# b = x
# print(a,b)


# lst = [88,6,546,95,4,71,9,32,1]
# for a in range(len(lst)):   #  记录内部排序的次数
#     i = 0
#     while i < len(lst)-1:   #  把最大值移动到有端
#         if lst[i] > lst[i+1]:   #  比较
#             lst[i],lst[i+1] = lst[i+1],lst[i]   #交换
#         i = i +1
# print(lst)


#  第三题
# from  random import randint     #  要用随机数, 必须导入这个
# # a = randint(0,20)   #  0-20 的随机数
# # print(a)
# s = set()
# while len(s) < 7:
#     s.add(randint(1,36))
# print(s)


#  第四题

