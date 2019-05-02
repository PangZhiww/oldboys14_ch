# s = "alex"
# abc = id(s)
# print(abc)

# lst = ["大秧歌","大阳哥","小花生","然哥"]
# print(id(lst))     #   就是一个内存地址, 毫无意义


# lst = ["周杰伦","然哥"]
# lst1 = ["周杰伦","然哥"]
# print(id(lst))
# print(id(lst1))
# 小数据池. 会对字符串进行缓存, 为了节省内存
#
# lst = ["然哥", "周杰伦"]
# lst1 = ["然哥", "周杰伦"]
# print(id(lst))
# print(id(lst1))


# a = {"df":"dfa","dafas":"dsaf"}
# b = {"dfs":"df","dfdhs":"krtaf"}
# print(id(a))
# print(id(b))
