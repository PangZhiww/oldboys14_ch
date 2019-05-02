
# def func(*args):
#     sum = 0
#     for el in args:
#         sum += el   # 求和
#     return sum

    # return sum(args)
# print(func(1,2,3))


# a = 10
# b = 20
# def text5(a,b):
#     print(a,b)
#     return text5
# print(text5(b,a))


# a = 10
# b = 20
# def text5(a,b):
#     a = 3
#     b = 5
# print(a,b)
# c = text5(b,a)
# print(c)


# def func(*args):
#     print(args)
# func(*[1,2,3],*(22,33))


# def func(**kwargs):
#     print(kwargs)
# func(**{'name':'alex'},**{'age':'1000'})


# def func(a,b):
#     c = a if a > b else b
#     return c
# print(func(5,66))


# def func(new_txt,*args):
#     s = '_'.join(args)
#     f = open(new_txt,mode='a',encoding='utf-8')
#     f.write(s)
#     f.flush()
#     f.close()
# func('new',*['1','老男孩','武sir'])



# def func(*args):
#     ma = args[0]
#     mi = args[0]
#     for el in args:
#         if el > ma:
#             ma = el
#         if el < mi:
#             mi = el
#     return {'最大值':ma,'最小值':mi}

# print(func(56,3,76,13,15,3,796,1,))


# def func(*args):
#     sum = 1
#     for i in args:
#         sum *= i
#     return sum
#
# print(func(7,8,5,3))


# def func():
#     yanse = ['红心','草花','方块','黑桃']
#     dianshu = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
#     result = []
#     for dian in dianshu:
#         # print(dian)
#         for yan in yanse:
#             # print(yan)
#             result.append((dian,yan))
#     return result
#
# print(func())
















