import json

# json格式的限制1, json格式的key必须是字符串数据类型
# json格式中的字符串只能是“”
# 如果是数字为key, 那么dump之后会强行转成字符串数据类型

# dic = {1:2,3:4}
# str_dic = json.dumps(dic)
# print(str_dic)
# print(type(str_dic))
#
# new_dic = json.loads(str_dic)
# print(new_dic)
# print(type(new_dic))
#
# print(dic)

# json是否支持元祖, 对元祖做value的字典会把元祖强制转换成列表
# dic = {"abc":(2,3,4)}
# str_dic = json.dumps(dic)
# print(str_dic)
# new_dic = json.loads(str_dic)
# print(new_dic)

# json是否支持元祖做key，不支持
# dic = {(1,2,3):"abc"}
# str_dic = json.dumps(dic)

# 对列表的dump
# lst = ["aaa","bbb",123,'ccc',12.456]
# with open("json_demp","w") as f:
#     json.dump(lst,f)
# with open('json_demp') as f:
#     ret = json.load(f)
#     print(ret)

# 能不能多次dump数据到文件里，可以多次dump但是不能load出来了
# dic = {"abc":(1,2,3)}
# lst = ["aaa","bbb",123,"ccc",12.456]
# with open("json_demp","w")as f:
#     json.dump(lst,f)
#     json.dump(dic,f)
# with open("json_demo")as f:
#     ret = json.load(f)
#     print(ret)

# 想dump多个数据进入文件，用dumps
# dic = {"abc": (1, 2, 3)}
# lst = ["aaa", "bbb", 123, "ccc", 12.456]
# with open("json_domp", "w")as f:
#     str_lst = json.dumps(lst)
#     str_dic = json.dumps(dic)
#     f.write(str_lst + "\n")
#     f.write(str_dic + "\n")
# with open("json_domp")as f:
#     for line in f:
#         ret = json.loads(line)
#         print(ret)

# 中文格式的 ensure——ASCII= False
# dic = {"abc":(1,2,3),"country":"中国"}
# ret= json.dumps(dic)
# # ret= json.dumps(dic,ensure_ascii=False)
# print(ret)
# dic_new = json.loads(ret)
# print(dic_new)

# dic = {"abc":(1,2,3),"country":"中国"}
# with open("json_demp","w",encoding="utf-8") as f:
#     json.dump(dic,f,ensure_ascii=False)


# json的其他参数，是为了用户看的更方便，但是会相对浪费储存空间
import json
data = {"username":["梨花","二愣子"],"sex":"male","age":83}
json_dic2 = json.dumps(data,sort_keys=True,indent=2,separators=(",",":"),ensure_ascii=False)
print(json_dic2)