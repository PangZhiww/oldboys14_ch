# 第二题
# def func(lst):
#     list = []
#     for i in range(len(lst)):
#         if i % 2 == 1:
#             list.append(lst[i])
#     return list
#
# a = [3,5,64,3,24,6]
# ret = func(a)
# print(ret)


# 第三题
# def func(a):
    # if len(a) > 5:
    #     return True
    # else:
    #     return False

    # return len(a) > 5



# 第四题
# def func(lst):
#     if len(lst) > 2:
#         return lst[0],lst[1]
#
# lst = [23,42,42,121,563,565,33,452]
# ret = func(lst)
# print(ret)


# 第五题
# def func(s=""):
#     shuzi = 0
#     zimu = 0
#     kongge = 0
#     qita = 0
#     for c in s:     # 循环字符串,拿到每个字符
#         if c.isdigit():     # 数字
#             shuzi += 1
#         elif c.isalpha():   # 字母
#             zimu += 1
#         elif c == " ":
#             kongge += 1
#         else:
#             qita += 1
#     return shuzi, zimu, kongge, qita
# s = "huewrq 86frlgjmaekior[]r74356+4+7984ew+r"
# ret = func(s)
# print(ret)


# 第六题
# def func(a,b):
    # if a>b:
    #     return a
    # else:
    #     return b
    # c = a if a > b else b     # 三元写法
    # return c
# print(func(5,99))


# 第七题
# dic = {"k1":"v1v2","k2":[11,22,33,44]}

# def func(dic):
#     new_dic = {}
#     for k,v in dic.items():
#         if len(v) > 2:
#             new_dic[k] = v[0:2]
#         else:
#             new_dic[k] = v
#     return new_dic
# dic = {"k1":"v1v2","k2":[11,22,33,44]}
# print(func(dic))


# 第八题
# def func(lst):
#     dic = {}
#     for i in range(len(lst)):
#         dic[i] = lst[i]
#     return dic
#
# lst = [56,96,12,56,74,3,745,6,1,747]
# print(func(lst))


# 第九题
# def func(name,age,edu,sex="男"):
#     f = open("student.msg",mode="a",encoding="utf-8")
#     f.write(name+"_"+age+"_"+edu+"_"+sex+"\n")
#     f.flush()
#     f.close()
#
# while 1:
#     content = input("请问是否要输入学生信息(退出请按Q):")
#     if content.upper() == "Q":
#         break
#     n = input("请输入姓名")
#     a = input("请输入年龄")
#     e = input("请输入学历")
#     s = input("请输入性别")
#     if s == "":
#         func(n,a,e)
#     else:
#         func(n,a,e,s)


# 第十题
# import os
# def func(filename,old,new):
#     with open(filename,mode="r",encoding="utf-8") as f1,\
#         open(filename+"_副本",mode="w",encoding="utf-8") as f2:
#
#         for line in f1:
#             s = line.replace(old,new)
#             f2.write(s)
#
#     os.remove(filename)
#     os.rename(filename+"_副本","filename")
#
# func("student.msg","学","本")


# 无名氏_96_男_小学
# 位置_85_大学_
# 王玺_82_大学_
# 王玺_29__大学
# 发_啥的份上_大双方都_
# dfarsags_adsfg__阿达
# 王雄_29_大学_男
