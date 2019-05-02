import time
# print(time.time())
# print(time.strftime("%Y-%m-%d"))
# time_obj = time.localtime()
# print(time_obj)
# print(time_obj.tm_year)
# print(time_obj.tm_mon)
# print(time_obj.tm_mday)
# print(time_obj.tm_hour)
# print(time_obj.tm_min)
# print(time_obj.tm_sec)
# print(time_obj.tm_wday)
# print(time_obj.tm_yday)

# print(time.strftime("%Y-%m-%d"))
# print(time.strftime("%Y-%m-%d %H:%M:%S %A"))
# print(time.strftime("%y-%m-%d %H:%M:%S %A"))


# struct_time = time.localtime()
# print(time.mktime(struct_time))
# ret = time.strftime("%Y-%m-%d %H:%M:%S",struct_time)
# print(ret)

# ret = time.strptime("2019-03-28","%Y-%m-%d")
# print(time.mktime(ret))
# print(ret)

ret = time.strftime("%Y-%m-1")
struct_time = time.strptime(ret,"%Y-%m-%d")
# print(struct_time)
print(time.mktime(struct_time))

steuct_time = time.localtime()
steuct_time = time.strptime("%s-%s-1" % (steuct_time.tm_year,steuct_time.tm_mon),"%Y-%m-%d")
print(time.mktime(steuct_time))