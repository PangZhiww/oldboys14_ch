
# 2
# def func(*args):
#     sum = 0
#     for el in args:
#         sum = sum + el
#     return sum
#
# print(func(1,2,3))


# def func(*args):
#     return sum(args)
# print(func(1,2,3))


# 第三题
# a = 10
# b = 20
# def test5(a,b):
#     print(a,b)
# c = test5(b,a)
# print(c)    # 没有返回值


# 第四题
# a = 10
# b = 20
# def test5(a,b):
#     a = 3
#     b = 5
# print(a,b)
# c = test5(b,a)
# print(c)    # 没有给返回值


# 第五题
# def func(*args):
#     print(args)
#
# func(*[1,2,3],*(22,33))


# 第六题
# def func(**kwargs):
#     print(kwargs)
#
# func(**{'name':'alex'},**{'age':1000})


# 第九题
# def func(new_txt,*args):
#     s = '_'.join(args)
#     f = open(new_txt,mode='a',encoding='utf-8')
#     f.write(s)
#     f.flush()
#     f.close()
#
# func('new_txt',*['1','老男孩','武sir'])


# 第十题
# 接受n个参数, 返回最大值和最小值(字典)
# def func(*args):
#     return {"最大值":max(args),'最小值':min(args)}

# def func(*args):
#     m = args[0]     # 假设第0项就是最大值
#     mi = args[0]
#     for el in args:
#         if el > m:
#             m = el      # 当前这个元素比假设的内个大, 记录当前的这个比较大的数
#         if el < mi:
#             mi = el
#     return {'最大值':m,'最下值':mi}
#
# print(func(4,5,64,7643,2,743))


# 第11题
# def func(*args):
#     sum = 1
#     for i in args:
#         sum = sum * i
#     return sum
#
# print(func(7*5*4*3*2*1))


# 第12题
# def func():
#     yanse = ["红心","草花","方块","黑桃"]
#     dianshu = ['A','2','3','4','5','6','7','8']
#     result = []
#     for el in yanse:
#         # print(el)
#         for dian in dianshu:
#             # print(dian)
#             result.append((el,dian))
#     return result
#
# print(func())


# 第13题
# def wrapper():
#     def inner():
#         print(666)
# wrapper()
#
# # 1
# def wrapper():
#     def inner():
#         print(666)
#     inner()
# wrapper()
#
# # 2
# def wrapper():
#     def inner():
#         print(666)
#     return  inner
# wrapper()()


# 第12题  2
# 如果默认值参数是一个可变的数据类型, 如果有人调用的时候改变了她,其他位置看到的也跟着改变了

# def extendList(val,list=[]):
#     list.append(val)
#     return list
# list1 = extendList(10)    # list = [10,'a']
# list2 = extendList(123,[])
# list3 = extendList('a')     # list = [10,'a']
#
# print('list1=%s' % list1)
# print('list2=%s' % list2)
# print('list3=%s' % list3)


# def extendList(val,list=[]):
#     list.append(val)
#     return list
# list1 = extendList(10)    # list = [10]
# print('list1=%s' % list1)
#
# list2 = extendList(123,[])
# print('list2=%s' % list2)
#
# list3 = extendList('a')     # list = [10,'a']
# print('list3=%s' % list3)


# 第12题
a = 1
while a <= 9:
    # print(a)
    b = 1
    while b <= a:
        print('%d*%d=%d\t' % (a,b,a+b),end='')
        b = b + 1
    print()
    a = a + 1


