# import re
#
# # findall
#
# # ret = re.findall("\d+","fa4f54a45er331")
# # ret = re.findall("\w+","fa4f54a45er331")
# # ret = re.findall("\s+","fa4f54a45er331")
# # print(ret)
# # ret = re.search("\d+","f78g5646t7854fd+578d564df")
# # ret = re.search("\w+","f78g5646t7854fd578d564df")
# # print(ret.group())
# # ret = re.search("\s+","f78g5646t7854fd578d564df")
# # print(ret)
# # print(type(ret))
# # if ret:
# #     print(ret.group())
# # else:
# #     print("没有值...")



import re

# findall

# ret = re.findall("\d+","191fgsf48484s8dfsfd8948")
# print(ret)
# print(type(ret))

# ret = re.findall("\s+","191fgsf48484s8dfsfd8948")
# print(ret)


# search
# ret = re.search("\d+","aaa1000d5f1d45f1df89848")
# ret = re.search("\s+","aaa1000d5f1d45f1df89848")
# print(ret.group())
# print(type(ret))
# print(ret)


# match
# ret = re.match("\d+","511gs89gfs184184")
# print(ret)
# print(type(ret))
# print(ret.group())


# 替换
# sub
# print("replace789dfw854fw85df56adqw".replace("w","H",2))
# ret = re.sub("\d+","H","replace789ds56")
# print(ret)
# ret = re.sub("\d+","H","replace789fdfad4456a5 f5d4f5df45645",3)
# print(ret)

# subn
# ret = re.subn("\d+","H","68replace789fdfad4456a5f5+d4f5df45645",5)
# print(ret)


# 切割
# split
# ret = re.split("\w+","68replace789fdfad4456a5 f5d4f5df45645")
# print(ret)


# 进阶方法
# compile         时间效率
# ret = re.compile("-[1-9]\d+(\.\d+)?|-(0\.)?[1-9](\.\d+)?")
# res = ret.search("fdadfa-68replace789fdfad4456a5 f5d4f5df45645")
# res = ret.match("-0.6replace789fdfad4456a5 f5d4f5df45645")
# print(res)
# print(res.group())

# finditer
# print(re.findall("\d+","68replace789fdfad4456a5 f5d4f5df45645"))
# ret = re.finditer("\d+","68replace789fdfad4456a5 f5d4f5df45645")
# print(ret)
# print(next(ret).group())
# print(next(ret).group())
# for r in ret:
#     print(r)
    # print(r.group())


# ret = re.compile("-0\.\d+|-[1-9]\d*(\.\d+)?")
# c = ret.search("-lasdada-200")
# c = ret.findall("-lasdada-200")
# print(c)
# print(c.group())
