import re

# ret = re.findall("www\.baidu\.com|www\.oldboy\.com","www.baidu.com")
# print(ret)
# ret1 = re.findall("www\.(?:baidu|oldboy)\.com","www.baidu.com")
# print(ret1)


# ret = re.compile("-0\.\d+|-[1-9]\d*(?:\.\d+)?")
# # c = ret.search("-1asdada-200")
# # print(c.group())
# c1 = ret.findall("-1asdada-200")
# print(c1)
#
# # c2 = re.search("-0\.\d+|-[1-9]\d*(\.\d+)?","-1asdada-200")
# # print(c2)
# # print(c2.group())
# ret1 = re.findall("-0\.\d+|-[1-9]\d*(\.\d+)?","-1asdada-200")
# print(ret1)


# ret = re.split("\d+","f564gsfd5g59s df4195ad4f")
# print(ret)
# ret1 = re.split("(\d+)","f564gsfd5g59sdf4195ad4f")
# print(ret1)


# 分组遇见search
# ret = re.search("\d+(\.\d+)(\.\d+)(\.\d+)?(\.\d+)?","1.2.3.4-2*(60+(-40.35/5)-(-4*3))")
# print(ret)
# print(ret.group())
# print(ret.group(1))
# print(ret.group(0))
# print(ret.group(2))
# print(ret.group(4))