import re

# ret=re.findall(r"\d+","1-2*(60+(-40.35/5)-(-4*3))")
# print(ret) #['1', '2', '60', '40', '35', '5', '4', '3']
# ret=re.findall(r"-?\d+\.\d*|(-?\d+)","1-2*(60+(-40.35/5)-(-4*3))")
# print(ret) #['1', '-2', '60', '', '5', '-4', '3']
# ret.remove("")
# print(ret) #['1', '-2', '60', '5', '-4', '3']

# ret = re.findall(r"\d+","1-2*(60+(-40.35/5)-(-4*3))")
# ret1 = re.findall(r"\d+(?:\.\d+)?","1-2*(60+(-40.35/5)-(-4*3))")
# print(ret)
# print(ret1)

# 利用分组优先
# ret2 = re.findall(r"\d+(?:\.\d+)|(\d+)","1-2*(60+(-40.35/5)-(-4*3))")
# ret3 = re.findall(r"\d+\.\d+|(\d+)","1-2*(60+(-40.35/5)-(-4*3))")
# print(ret3)
# ret3.remove("")
# print(ret3)





import re

# ret = re.findall(r"<(\w+)>","<a>wahaha</a>")
# ret1 = re.findall\
#     (r"<\w+>(\w+)<","<a>wahaha</a>")
# print(ret)
# print(ret1)


# ret = re.search(r"<(\w+)>(\w+)<\\(\w+)>",r"<a>wahaha</a>")
# ret = re.search(r"<(\w+)>\w+<(/\w+)>","<a>wahaha</a>")
# print(ret.group())
# print(ret.group(1))
# print(ret.group(2))




# 分组命名

# ret = re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>")
# #还可以在分组中利用?<name>的形式给分组起名字
# #获取的匹配结果可以直接用group('名字')拿到对应的值
# print(ret.group('tag_name'))  #结果 ：h1
# print(ret.group())  #结果 ：<h1>hello</h1>
#
# ret = re.search(r"<(\w+)>\w+</\1>","<h1>hello</h1>")
# #如果不给组起名字，也可以用\序号来找到对应的组，表示要找的内容和前面的组内容一致
# #获取的匹配结果可以直接用group(序号)拿到对应的值
# print(ret.group(1))
# print(ret.group())  #结果 ：<h1>hello</h1>




# ret = re.search(r"<(?P<name>\w+)>(?P<c>\w+)<(/\w+)>","<a>wahaha</a>")
# print(ret.group())
# print(ret.group("name"))
# print(ret.group("c"))