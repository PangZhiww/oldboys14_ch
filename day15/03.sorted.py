# lst = [5,7,6,12,1,13,9,18,5]
# lst.sort()    # sort是list里面的一个方法
# print(lst)

# ll = sorted(lst)    # 内置函数, 返回给你一个新列表   新列表是被排序的
# ll = sorted(lst,reverse=True)    # 内置函数, 返回给你一个新列表   新列表是被排序的
# print(ll)


# 给列表排序. 根据字符串的长度进行排序
# lst = ['大阳哥','尼古拉斯','赵四','刘能','广坤','谢大脚']
#
# def func(s):
#     return len(s)   # 返回数字
#
# ll = sorted(lst,key=func,reverse=False)
# print(ll)


# lst = ['大阳哥','尼古拉斯','赵四','刘能','广坤','谢大脚']

# ll = sorted(lst,key=lambda s:len(s),reverse=False)
# print(ll)


# lst = ['大阳哥aaa','尼古拉斯a','赵aaaaaaa四','刘能aaaa','广坤aa','谢大aaaaaaaaaa脚']

# ll = sorted(lst,key=lambda s:s.count('a'))    # 内部, 把可以迭代对象中的内一个元素传递给func
# print(ll)


lst = [
    {'id':1, 'name':'alex', 'age':18},
    {'id':2, 'name':'taibai', 'age':88},
    {'id':3, 'name':'wusir', 'age':58},
    {'id':4, 'name':'ritian', 'age':48},
    {'id':5, 'name':'女神', 'age':8}
]

# def func(dic):
#     return dic['age']
# ll = sorted(lst,key=func)
# print(ll)

ll = sorted(lst,key=lambda dic:dic['age'])
print(ll)