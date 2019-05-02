#   教材课后练习
# dict = {
#     "name": ["alex", 2, 3, 5],
#     "job": "teacher",
#     "oldboy": {
#         "alex": ["python1", "python2", 100]}
# }
# dict["name"].append("wusir")
# # print(dict["name"])
#
# s1 = dict["name"][0].capitalize()
# dict["name"][0] = s1
# # print(s1)
#
# dict["oldboy"].setdefault("老男孩","linux")
# #
# dict["oldboy"]["alex"].remove("python2")
# print(dict)


#  作业
# print("dfads","dadf","sdsa",end=" bv ")
# print("sdfasd","DAf")


#  第一题
# tu = (
#     "alex",
#     [11,
#      22,
#      {"k1": "v1",
#       "k2": ["age", "name"],
#       "k3": (11, 22, 33)
#       },
#      44]
# )
# # tu[1][2]["k2"].append("Seven")
# print(tu)


#   第二题
# dic = {"k1": "v1",
#        "k2": "v2",
#        "k3": [11, 22, 33]
#        }
# for k in dic:
#        print(k)
#
# for k,v in dic.items():
#        print(v)
#        print(k,v)
#
# dic["k4"] = ["v4"]
#
# # dic["k1"] = "alex"

# dic["k3"].append("44")

# dic["k3"].insert(1,14)
# print(dic)


#    第三题
# av_catalog = {
#     "欧美":{
#         "www.youporn.com":["很多免费的,世界最大的","质量一般的"],
#         "www.pornhub.com":["很多免费的,也很大","质量比前面的好点"],
#         "letmedothistoyou.com":["多是自拍的,高质量图片很多","资源不多,更新慢"],
#         "x-art.com":["质量很高,真的很高","全部收费,屌丝请绕过"]
#     },
#     "日韩":{
#         "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]
#     },
#     "大陆":{
#         "1024":["全部免费,真好,好人一生平安","服务器在国外慢"]
#     }
# }
# av_catalog["欧美"]["www.youporn.com"].insert(1,"量很大")
# av_catalog["欧美"]["x-art.com"].remove("全部收费,屌丝请绕过")
# av_catalog["欧美"]["x-art.com"].append("金老板最喜欢这个")
# av_catalog["日韩"]["tokyo-hot"][1] = av_catalog["日韩"]["tokyo-hot"][1].upper()
# av_catalog["大陆"]["1048"] = ["一天就封了"]
# av_catalog["欧美"].pop("letmedothistoyou.com")
# av_catalog["大陆"]["1024"].insert(0,"可以爬下来")
# av_catalog["大陆"]["1024"][0] = av_catalog["大陆"]["1024"][0] + "可以爬下来"
# print(av_catalog)


#   第四题
# s= "k:1|k1:2|k2:3|k3:4"
# lst = s.split("|")    #   ['k:1']
# print(lst)
# dict = {}
# for el in lst:
#     # print(el)
#     k,v = el.split(":")
#     # print(k,v)
#     dict[k] = int(v)
# print(dict)


#    第五题
# set = {"k1":"","k2":""}
# ss = []
# dd = []
# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# for s1 in li:
#     if s1 > 66:
#         # print(s1)
#         ss.append(s1)
#         set["k1"] = ss
#     if s1 < 66:
#         # print(s1)
#         dd.append(s1)
#         set["k2"] = dd
#     # print(s1)
# print(set)


#   老师写的第五题
# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# dict = {"k1":[],"k2":[]}
# for el in li:
#     if el > 66:
#         dict["k1"].append(el)
#     elif el < 66:
#         dict["k2"].append(el)
#     else:
#         pass
# print(dict)


# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# dict = {}
# for el in li:
#     if el > 66:
#         dict.setdefault("k1",[]).append(el)
#     elif el < 66:
#         dict.setdefault("k2",[]).append(el)
#     else:
#         pass
# print(dict)


#   第六题
# goods = [
#     {"name": "电脑", "price": 1999},
#     {"name": "鼠标", "price": 10},
#     {"name": "游艇", "price": 20},
#     {"name": "美女", "price": 998},
# ]
# for i in range(len(goods)):
#     # print(i)
#     good = goods[i]
#     # print(good)
#     print(i + 1, good["name"], good["price"])
# # print(goods)
#
# while 1:
#     content = input("请输入你要买的商品序号:")
#     if content.upper() == "Q":
#         break
#     index = int(content) - 1  # 索引
#     if index > len(goods) - 1 or index < 0:     #   调试
#         print("输入有误,请重新输入:")
#         continue
#     print("您选择的是:", goods[index]["name"], goods[index]["price"], "元")
#
#
#
