# s = {"王者荣耀","英雄联盟","王者荣耀",123,True,True}
# print(s)    #   不重复的 | 无序的


# lst = {"张强","刘洋","李强","王磊","刘伟","张强","张伟","刘洋","张伟"}
# s = set(lst)    #  去重复
# print(s)

#   变回来
# lst = list(s)
# print(lst)


# lst = {"张强","刘洋","李强","王磊","刘伟","张强","张伟","刘洋","张伟"}
# lst.update("马化腾")     #   迭代更新
# lst.update("马化腾","我会")     #   迭代更新
# print(lst)


#  冻结了的set集合,可哈希的,不可变
s = frozenset([1,3,6,6,9,8])    #  可以去重复,也是set集合
print(s)
#
ss = {"a" ,s}
print(ss)
