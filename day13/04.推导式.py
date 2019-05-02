# 生成列表 里面装1-14期的数据
# lst = []
# for i in range(1,16):
#     lst.append('python%s' % i)
# print(lst)

# 列表推倒式: 最终给你的是列表
# 语法 [最终结果(变量) for 变量 in 可迭代对象]

# lst = [i for i in range(1,15)]
# lst = ['python%s' % i for i in range(1,15)]
# print(lst)


# 筛选模式
# [最终结果 for 变量 in 可迭代对象 if 条件]
# 1. 获取1-100以内能被3整除的数
# lst = [i for i in range(1,101) if i % 3 == 0]
# print(lst)
# 2. 100以内能被3整除的数的平方
# lst = [i**2 for i in range(1,101) if i % 3 == 0]
# print(lst)
# 3. 寻找名字中带有两个e的人的名字
# names = [['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Job'],['Alice','Jill','Ana','Wendy','Jennifer','Sherry','Eva']]
# lst = [name for first in names for name in first if name.count('e') == 2]
# print(lst)

lst = ['衣服%s' % i for i in range(1000)]
print(lst)