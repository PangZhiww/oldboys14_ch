# def func(i):
#     return i % 2 == 1
# lst = [1,2,3,4,5,6,7,8,9]
#
# ll = filter(func, lst)
# ll = filter(lambda i:i%2 == 1, lst)

# print('__iter__' in dir(ll))
# print('__next__' in dir(ll))

# print(list(ll))


# lst = [
#     {'id':1, 'name':'alex', 'age':18},
#     {'id':2, 'name':'taibai', 'age':88},
#     {'id':3, 'name':'wusir', 'age':58},
#     {'id':4, 'name':'ritian', 'age':48},
#     {'id':5, 'name':'女神', 'age':8}
# ]
#
# print(list(filter(lambda dic:dic['age']>40,lst)))