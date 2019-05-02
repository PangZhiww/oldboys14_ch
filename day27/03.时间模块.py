import time

# 时间戳时间, 格林威治时间, float数据类型      给机器用的
    # 英国伦敦时间    1970.1.1.0:0:0
    # 北京时间    1970.1.1.8:0:0
    # 1553664650.4697165

# 结构化时间, 时间对象   从给机器看的转换为给人看的(上下两种格式的中间状态)
    # 时间对象. 能够通过,属性名来获取对象中的值
# 格式化时间, 字符串时间, str数据类型     给人看的
    # 可以根据你需要的格式, 来显示时间

# print(time.time())  # 时间戳时间
# print(time.strftime("%Y-%m-%d"))    # 格式化时间 time.strformat time --> ime.strftime
# time_obj = time.localtime()     # 对象数据结构时间
# print(time_obj)
# print(time_obj.tm_year)
# print(time_obj.tm_mday)
# print(time_obj.tm_mon)
# print(time_obj.tm_hour)
# print(time_obj.tm_min)
# print(time_obj.tm_sec)
# print(time_obj.tm_wday)
# print(time_obj.tm_yday)


# print(time.strftime("%Y-%m-%d %H:%M:%S %A"))
# print(time.strftime("%y-%m-%d %H:%M:%S %A"))
# print(time.strftime("%c"))



# 计算本月一号的时间戳时间
# 时间戳时间
# 结构化时间
# struct_time = time.localtime()
# struct_time = time.strptime("%s-%s-1" % (struct_time.tm_year,struct_time.tm_mon),"%Y-%m-%d")
# print(time.mktime(struct_time))
# # 格式化时间
# ret = time.strftime("%Y-%m-1")
# struct_time = time.strptime(ret,"%Y-%m-%d")
# print(struct_time)
# print(time.mktime(struct_time))

