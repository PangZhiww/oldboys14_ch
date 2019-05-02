# dict = {"及时雨":"松江","小李广":"华容","黑旋风":"李逵","易大师":"剑圣","花和尚":"鲁智深"}

# print(dict)
# print(dict.keys())  #  拿到所有的key, 返回key的集合, 像是列表, 但不是列表
# for key in dict.keys():    #  可以进行迭代循环
#     print(key)

# print(dict.values())    #  拿到所有的value,返回value的集合,像是列表,但是不是列表
# for value in dict.values():
#     print(value)

# print(dict.items())    #  拿到键值对
# for item in dict.items():
#     # print(item)
#     # print(item[0])    #  key
#     print(item[1])      #  value

dict = {"及时雨":"松江","小李广":"华容","青面兽":"杨志"}
# print(dict.items())
# for item in dict.items():       #1
    # k,v = item    #  1
    # print(item)
    # print(k)      #1
    # print(v)      #1
#   遍历dict
for k,v in dict.items():
    print(k,v)
# for k in dict:
#     print(k)

# 解构, 解包
# a,b = (1,2)
# print(a)
# print(b)
# print(a,b)

# a,b,c = ("马虎疼","马化腾","麻花藤")
# print(b)

# a,b = [1,2]
# print(a)
# print(b)
# print(a,b)