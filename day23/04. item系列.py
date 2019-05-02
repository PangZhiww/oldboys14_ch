# item系列和对象使用[]访问值有联系

# obj = {"k":"v"}
# print(obj)
# print(obj["k"])

# class B:
#     def __getitem__(self, item):
#         print('执行我啦',item)
#         return "bbbbbb"
#
# b = B()
# # b["a"]
# print(b["a"])
# print(b["k"])


# class B:
#     def __getitem__(self, item):
#         print('执行我啦', item)
#         return "bbbbbb"
#     def __setitem__(self, key, value):
#         print(key,value)
# b = B()
# # print(b["a"])
# # print(b["k"])
# b["k"] = "value"
# print(b["k"])

# 在内置的模块中, 有一些特殊的方法, 要求对象必须实现__getitem__/__setitem__才能使用
# class B:
# #     def __getitem__(self, item):
# #         return getattr(self,item)
# #     def __setitem__(self, key, value):
# #         setattr(self,key,value)
# # b = B()
# # b["k1"] = "v1"
# # b.k2 = "v2"
# # print(b.k2)
# # print(b.k1)
# # print(b["k1"])


# class B:
#     def __getitem__(self, item):
#         return getattr(self,item)
#     def __setitem__(self, key, value):
#         setattr(self,key,value)
#     def __delitem__(self, key):
#         # print(key)    # 删不掉用下面的方法
#         delattr(self,key)
# b = B()
# # b["k1"] = "v1"
# # b.k2 = "v2"
# # print(b.k2)
# b["k1"] = "v1"  # __setitem__
# print(b["k1"])  # __getitem__
# del b["k1"]     # __delitem__
# print(b["k1"])



# class B:
#     def __init__(self,lst):
#         self.lst = lst
#     def __getitem__(self, item):
#         return self.lst[item]
#     def __setitem__(self, key, value):
#         self.lst[key] = value
#     def __delitem__(self, key):
#         self.lst.pop(key)
# b = B(["111","222","ccc","ddd"])
# print(b.lst[0])
# print(b[0])
# b[3] = "alex"
# print(b[3])
# print(b.lst)
# del b[2]
# print(b.lst)


# 类
# 每个对象都是一副扑克牌
# 我想查看这个对象, 来查看整副牌
# 我想从这一副牌中随机抽取一张牌
# 我想完成打乱这副牌的顺序功能