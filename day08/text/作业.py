#  第一题
# 老男孩是最好的培训机构,
# 全心全意为学生服务,
# 只为学生未来,不牟利.
# 我说的都是真的.哈哈


# f = open("a1.txt",mode="r",encoding="utf-8")
# s = f.read()
# print(s)
# f.flush()
# f.close()


# f = open("a1.txt",mode="a",encoding="utf-8")
# f.write("信不信由你,反正我信了")
# f.flush()
# f.close()

# f = open("a1.txt",mode="r+",encoding="utf-8")
# s = f.read()
# f.write("信不信由你,反正我信了")
# print(s)
# f.flush()
# f.close()


# f = open("a1.txt",mode="w",encoding="utf-8")
# f.write("每天坚持一点,\n每天努力一点,\n每天多思考一点,\n慢慢你会发现,\n你的进步越来越大.")
# f.flush()
# f.close()


# import os
# with open("a1.txt",mode="r",encoding="utf-8") as f1,\
#     open("a1_new.txt",mode="w",encoding="utf-8") as f2:
#     s = f1.read()
#     ss = s.replace("我说的都是真的.哈哈","你们就信吧~\n我说的都是真的.哈哈")
#     f2.write(ss)
# os.remove("a1.txt")
# os.rename("a1_new.txt","a1.txt")


#  第二题
# 葫芦娃,葫芦娃,
# 一根藤上七个瓜
# 风吹雨打,都不怕,
# 啦啦啦啦.
# 我可以算命,而且算的特别准:
# 上面的内容你肯定是心里默唱出来的,对不对?哈哈

# f = open("t1.txt",mode="r+",encoding="utf-8")
# f.read()
# f.write("13")
# for line in f:
#     print(line)
# f.flush()
# f.close()


# f = open("t1.txt",mode="r",encoding="utf-8")
# for line in f:
#     print(line)
#
# f.flush()
# f.close()


# f = open("t1.txt",mode="r",encoding="utf-8")
# for line in f:
#     a = f.readlines()
#     print(a)
#
# f.flush()
# f.close()


# f = open("t1.txt",mode="r",encoding="utf-8")
# s = f.read(4)
# print(s)
# f.flush()
# f.close()


# f = open("t1.txt",mode="r",encoding="utf-8")
# s = f.readline().split()
# print(s)
# f.flush()
# f.close()


# f = open("t1.txt",mode="r",encoding="utf-8")
# a = f.readlines()
# print(a)
# print(a[2:])
#
# f.flush()
# f.close()


# f = open("t1.txt",mode="a+",encoding="utf-8")
# f.write("\n老男孩教育")
# f.seek(0)
# a = f.read()
# print(a)
# f.flush()
# f.close()


# f = open("t1.txt",mode="r+",encoding="utf-8")
# f.seek(20)
# print(f.tell())
# f.truncate()
#
# f.flush()
# f.close()


#  第三题
# apple 10 3
# tesla 100000 1
# mac 3000 2
# lenovo 30000 3
# chicken 10 3

# f = open("a3.txt",mode="r",encoding="utf-8")
# line = f.readline()
# lst = line.split()
# print(lst)
#
# result = []
# for lin in f:
#     ll = lin.split()
    # print(ll)
#
    # dict = {}
    # for i in range(len(ll)):
    #     dict[lst[i]] = ll[i]
    # result.append(dict)
# print(result)
#
# f.flush()
# f.close()


#  第四题
# Alex是老男孩Python发起人,创建人.
# Alex其实是人妖.
# 谁说Alex是sb?
# 你们真逗,Alex再牛逼,也掩饰不住资深屌丝的气质.

# import os
# with open("a4.txt",mode="r",encoding="utf-8") as f1,\
#     open("a4_new.txt",mode="w",encoding="utf-8") as f2:
#     for s in f1:
#         a4_new = s.replace("Alex","SB")
#         f2.write(a4_new)
# os.remove("a4.txt")
# os.rename("a4_new.txt","a4.txt")


#  第五题






#  第六题.
# 序号    部门    人数    平均年龄    备注
# 1     pyrhon   30      26       单身狗
# 2     Linux    26      30       屌丝狗
# 3     运营部    20      24       单身狗

# f = open("a6.txt",mode="r",encoding="utf-8")
# line = f.readline()
# lst = line.split()     #  第一行切割完成  key 就准备完了

# result = []
# 接着的向后读取
# for lin in f:
#     ll = lin.split()     # 每一行都进行切割
    # print(ll)
    # dic = {}
    # for i in range(len(ll)):    #  i 表示 ll 的索引
        # lst[i]      # key
        # ll[i]       # value
        # dic[lst[i]] = ll[i]
    # result.append(dic)
# print(result)

# f.flush()
# f.close()

