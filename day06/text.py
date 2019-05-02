#   第一题
# for i in range(1,11):
#     fen = input("请评委%d打分:"% i)
#     if int(fen) > 5 and int(fen) < 10:
#         print("OK的分数!")
#     else:
#         print("不在有效范围")

# i = 1
# while i < 11:
#     fen = input("请评委%d打分:" % i)
#     if int(fen) > 5 and int(fen) < 10:
#         print("OK的分数!")
#     else:
#         print("不在有效范围")
#         continue
#     i = i + 1


#   第二题
# lst = ["金瓶梅","解救吾先生","美国往事","西西里的美丽传说"]
# dict = {}
# for el in lst:
#     # print("请给%s电影进行打分:"% el)
#     fen = input("请给%s电影进行打分:" % el)
#     dict[el] = fen
# print(dict)


#   第三题
# dic = {
#     '-':"fu",
#     '0':'ling',
#     '1':'yi',
#     '2':'er',
#     '3':'san',
#     "4":"si",
#     '5':'wu',
#     "6":"liu",
#     "7":"qi",
#     "8":"ba",
#     "9":"jiu",
#     ".":"dian",
#     "+":"zheng",
# }
# # for i,y in dic.items():
# #     print(i,y)
# content = input("请输入一个数字:")
# for c in content:
#     print(dic[c],end=" ")


#   第五题
# zhubo = {"卢本伟":999999,"冯提莫":1400000,"陈一发儿":15000000,"金老板":4500}
#   1. 计算平均收益
# sum = 0
# for value in zhubo.values():
#     sum = sum + value
# print(sum/len(zhubo))
#
# avg = sum / len(zhubo)    #   平均值
#
# #   循环的时候记录要删除的key
# lst = []
# for k, v in zhubo.items():
#     if v < avg:
#         lst.append(k)     #   列表保存要删除的key
# for el in lst:    #   迭代的是列表
#     zhubo.pop(el)     #   删的是字典
# print(zhubo)

# zhubo.pop("卢本伟")
# print(zhubo)

