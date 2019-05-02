# 序列化
# 归一化
# 实例化
# 初始化
# 国际化
# 白热化
# 都市化


# 序列化
    # 序列指: 列表 元祖 字符串
    # 得到一个字符串的结果, 过程叫做序列化
# 字典/列表/数字/对象 --> 字符串   这个过程就叫做 序列化
# 为什么要序列化
    # 1. 要把内容写入文件   序列化
    # 2. 网络传输数据     序列化

# 字符串 - 反序列化 -> 字典/列表/数字/对象     这个过程叫做 反序列化

# 方法
# dic = {"k":"v"}
# print(str(dic))
# print([str(dic)])

# str_dic = str(dic)
# print(eval(str_dic))
# eval不能随便用

# json
import json
# dic = {"aaa":"bbb","ccc":"ddd"}
# str_dic = json.dumps(dic)
# print(dic)
# print([str_dic])
# print(str_dic,type(str_dic))
# with open("json_dump","w") as f:
#     f.write(str_dic)
# ret = json.loads(str_dic)
# print(ret,type(ret))
# print(ret["aaa"])


dic = {"aaa":"bbb","ccc":"ddd"}
with open("json_dump2","w") as f:
    json.dump(dic,f)

with open("json_dump2") as f:
    print(type(json.load(f)))
