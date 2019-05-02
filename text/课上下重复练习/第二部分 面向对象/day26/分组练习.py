import re

# ret = re.findall("-?\d+", "1-2*(60+(-40.35/5)-(-4*3))")
# ret = re.findall("\d+", "1-2*(60+(-40.35/5)-(-4*3))")
# print(ret)
# ret1 = re.findall(r"\d+", "1-2*(60+(-40.35/5)-(-4*3))")
# print(ret1)
# ret2 = re.findall(r"-?\d+\.\d*|(-?\d+)","1-2*(60+(-40.35/5)-(-4*3))")
# print(ret2)
# ret2.remove("")
# print(ret2)


# ret = re.findall(r"\d+","1-2*(60+(-40.35/5)-(-4*3))")
# print(ret)


# ret = re.findall(r"(\d+)|-?\d+\.\d+","1-2*(60+(-40.35/5)-(-4*3)")
# ret2 = re.findall(r"-?\d+\.\d+|(\d+)","1-2*(60+(-40.35/5)-(-4*3)")
# print(ret)
# print(ret2)
# ret1 = re.findall(r"-?\d+(?:\.\d+)?","1-2*(60+(-40.35/5)-(-4*3)")
# print(ret1)


# 利用分组优先
# ret = re.findall(r"\d+(?:\.\d+)|(\d+)","1-2*(60+(-40.35/5)-(-4*3)")
# print(ret)
# ret.remove("")
# print(ret)
# ret1 = re.findall(r"\d+\.\d+|(\d+)","1-2*(60+(-40.35/5)-(-4*3)")
# print(ret1)


# ret =  re.findall(r"<(\w+)>","<a>wahaha</a>")
# ret =  re.findall(r"<\w+>(\w+)<","<a>wahaha</a>")
# ret =  re.findall(r">(\w+)<","<a>wahaha</a>")
# print(ret)

# ret = re.search(r"<(\w+)>(\w+)<\\(\w+)>","<a>wahaha</a>")
# ret = re.search(r"<(\w+)>(\w+)<(/\w+)>",r"<a>wahaha</a>")
# print(ret)
# print(ret.group())
# print(ret.group(1))
# print(ret.group(2))
# print(ret.group(3))


# 分组命名
# ret = re.search(r"(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>Hello</h1>")
# print(ret.group("tag_name"))
# ret = re.search(r"<(?P<top_name>\w+)>\w+</(?P=top_name)>","<a1>wahaha</a1>")
# ret = re.search(r"<(\w+)>(\w+)</(\1)>","<a1>wahaha</a1>")
# print(ret.group("top_name"))
# print(ret.group(1))
# print(ret.group(2))
# print(ret.group(3))


# ret = re.search(r"<(?P<name>\d+)>(\w+)</(\1)>","<233>wahaha</233>")
# print(ret.group("name"))
# print(ret.group(1))
# print(ret.group(2))
# print(ret.group(3))