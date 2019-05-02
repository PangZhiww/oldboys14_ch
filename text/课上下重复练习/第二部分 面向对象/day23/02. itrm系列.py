# class B:
#     def __getitem__(self, item):
#         print("执行我啦")
#         return "bbb"
#     def __setitem__(self, key, value):
#         print(key,value)
# b = B()
# b["a"]
# print(b["a"])
# print(b["k"])
# print(b["c"])

# b["k"] = "v1"
# print(b["k"])
# b["c"] = "b1"
# print(b["c"])
# b["a"] = "d1"
# print(b["a"])
# b["k1"] = "v1"
# print(b["k1"])

# b.k2 = "v2"
# print(b.k2)
# b.e2 = "aq"
# print(b.e2)
# b.p1 = "qq"
# print(b.p1)
# b.qq = "valun"
# print(b.qq)


# class B:
#     def __getitem__(self, item):
#         return getattr(self,item)
#     def __setitem__(self, key, value):
#         setattr(self,key,value)
#     def __delitem__(self, key):
#         delattr(self,key)
# b = B()
# b["k1"] = "v1"
# print(b["k1"])
# b.k3 = "v3"
# print(b.k3)
# b.k2 = "v2"
# print(b.k2)


# b["k1"] = "v1"
# b.k2 = "v2"
# print(b.k2)
# b["k1"] = "v1"
# print(b["k1"])
# del b["k1"]
# print(b["k1"])
# b["p1"] = "a1"
# print(b["p1"])
# b["aa"] = "ab"
# print(b["aa"])
# del b["aa"]
# print(b["aa"])


class B:
    def __init__(self,lst):
        self.lst = lst
    def __getitem__(self, item):
        return self.lst[item]
    def __setitem__(self, key, value):
        self.lst[key] = value
    def __delitem__(self, key):
        self.lst.pop(key)
b = B(["111","222","333","444","555"])
print(b.lst)
print(b.lst[1])
b[2] = "qqq"
print(b.lst)
b[3] = "alex"
print(b.lst)
del b[3]
print(b.lst)