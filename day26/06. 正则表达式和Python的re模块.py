import re

# ret = re.compile("-0\.\d+|-[1-9]\d*(?:\.\d+)?")   # 分组优先显示
# c = ret.search("-1asdada-200")
# print(c.group())
# c1 = ret.findall("-1asdada-200")
# c2 = re.search("-0\.\d+|-[1-9]\d*(\.\d+)?","-1asdada-200")  # 没有分组优先的限制
# print(c1)
# print(c2.group())

# ret = re.findall("-0\.\d+|-[1-9]\d*(?:\.\d+)?","-1asdada-200")
# print(ret)


# 分组优先
# ret = re.findall("www.baidu.com|www.oldboyedu.com","www.oldboyedu.com")
# print(ret)
# ret1 = re.findall("www\.(?:baidu|oldboyedu)\.com","www.oldboyedu.com")
# print(ret1)



# ret = re.split("\d+","alex83egon20taibai40")
# print(ret)
# ret1 = re.split("(\d+)","alex83egon20taibai40")
# print(ret1)


# 分组遇见search
# ret = re.search("\d+(\.\d+)(\.\d+)(\.\d+)?","1.2.3.4-2*(60+(-40.35/5)-(-4*3))")
# print(ret.group())
# print(ret.group(0))
# print(ret.group(1))
# print(ret.group(2))
# print(ret.group(3))