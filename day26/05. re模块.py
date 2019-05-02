import re

# 字符串
# 匹配
# findall   *****
# ret = re.findall("\d+","199251dsf5a4s85646")
# print(ret)  # 参数   返回值类型(列表)   返回值个数1    返回值内容(所有匹配上的项)
# print(type(ret))
# ret1 = re.findall("\s+","199251dsf5a4s85646")
# print(ret1)     # 返回一个空列表
# print(type(ret1))

# search    *****
# ret2 = re.search("\d+","199251dsf5a4s85646")
# if ret2:
#     print(ret2)   # 参数    返回值类型: 正则匹配结果的对象   返回值个数: 1   返回值内容: 如果匹配上了, 就返回对象
# else:
#     print("没有search方法")
# print(type(ret2))
# print(ret2.group())     # 返回的对象通过group来获取匹配到的第一个结果
# ret3 = re.search("\s+","199251dsf5a4s85646")
# print(ret3)   # 参数    返回值类型: None   如果没有匹配上, 就返回None
# print(type(ret3))

# match     **      永远都是从头匹配,其他跟search一样
# ret4 = re.match("\d+","199251dsf5a4s85646")
# ret4 = re.match("\d+","$%#199251dsf5a4s85646")
# print(ret4)
# print(type(ret4))
# print(ret4.group())
# ret5 = re.match("\d+","$%#199251dsf5a4s85646")
# print(ret5)

# 替换    replace
# sub   ***
# print("replace789w856w64546w456asdwsda".replace("w","H",3))
# ret = re.sub("\d+","H","replace789")
# ret1 = re.sub("\d+","H","replace789fdfad4456a5f5+d4f5df45645",3)
# print(ret)
# print(ret1)

# subn  ***
# ret = re.subn("\d+","H","replace7895f4d512fd5f1a416d5s452c5")
# ret1 = re.subn("\d+","H","replace7895f4d512fd5f1a416d5s452c5",3)
# print(ret)
# print(ret1)
#
# 切割
# split   ***
# ret = re.split("\d+","alex83egon20taibai40")
# print(ret)

# 进阶方法  - 爬虫\自动化开发
# compile   *****   时间效率
# "\d+" --> python解释器能理解的代码 --> 执行代码
# ret = re.compile("-[1-9]\d+(\.\d+)?|-(0\.)?[1-9](\.\d+)?")   # 欲编译功能   节省时间: 多次使用某一个相同的正则表达式的时候, 这个compile才会帮助我们提高程序的效率
# res = ret.search("doj5653fhfd46-5062f5df4d-4645")
# res1 = ret.search("-2df855d74f5df89-f419d48*-d+q-15dfcasd9d")
# print(res)
# print(res.group())
# print(res1.group())

# finditer  *****   空间效率
# print(re.findall("\d","f45e456ewrg96fd8ger456dfg654gfd"))
# ret = re.finditer("\d","fdagd45f54d575fd4f5d478sg96569fd74")
# print(ret)
# for r in ret:
    # print(r)
    # print(r.group())




# ret = re.compile("-0\.\d+|-[1-9]\d*(\.\d+)?")
# c = ret.search("-1asdada-200")
# print(c.group())
# c1 = ret.findall("-1asdada-200")
# print(c1)