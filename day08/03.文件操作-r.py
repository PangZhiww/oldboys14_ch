#  路径有两种:
#  1. 相对路径,相当于你当前程序所在的文件夹.(必须掌握)
#   ../ 返回上一层目录
#   相对的是当前程序所在的文件夹

#  2. 绝对路径, 1. 从磁盘根目录寻找. 2. 互联网上的一个绝对路径

#
# f = open("歌姬",mode="r",encoding="utf-8")
# s = f.read()
# f.close()   #  关闭句柄
# print(s)
#
# f = open("file/wuse",mode="r",encoding="utf-8")
# s = f.read()
# f.close()   #  关闭句柄
# print(s)


# f = open("吃的",mode="r",encoding="utf-8")
# s = f.readline()
# s1 = f.readline()
# f.flush()
# f.close()   #  关闭句柄
# print(s)
# print(s1)

# f = open("吃的",mode="r",encoding="utf-8")
# for line in f:      #  每次读取一行, 赋值给前面的line变量
#     print(line)
#     input("<<<")
# f.close()



f = open("吃的",mode="r",encoding="utf-8")
count = 0
for line in f:      #  每次读取一行, 赋值给前面的line变量
    if count != 5:
        count = count + 1
        continue
    else:
        print(line)
    count = count + 1
f.flush()
f.close()

