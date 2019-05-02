# def func():
#     print('你吃了吗吗?')
#
# print(func)
# a = func    # 函数名就是一个变量
# print(a)
# func()
# a()     # 就是一个函数的调用

# def a():
#     print("我吃了")

# func = a
# func()


# def f1():
#     print("我是马化腾")
# def f2():
#     print('我是马云')
# def f3():
#     print("我是马赛克")
# def f4():
#     print("我是马冬梅")

# lst = [f1,f2,f3,f4]
# print(lst)

# for el in lst:
#     el()
# lst = [f1(),f2(),f3(),f4()]
# print(lst)



# 还可以作为函数的参数
# def func(food):
#     print('吃',food)
#
# a = '火锅'
# func(a)




# def func(fn):
#     fn()
#
# def gn():
#     print('我是火锅,刚刚有人要吃我')
#
# func(gn)    # 可以把函数作为参数, 传递给另一个函数



# def func():
#     def inner():
#         print('火锅不让吃了,吃了上火')
#     return inner

# func()()

# ret = func()    # 这里func()执行之后获取到的是inner函数
# print(func)
# ret()   # 在理是让inner函数执行

# 综上, 函数就是一个变量


# def func():
#     print("吃了了么")
# #
# def func2(fn):
#     print("我是func2")
#     fn()    # 执⾏行行传递过来的fn
#     print("我是func2")
# func2(func)    # 把函数func当成参数传递给func2的参数fn.


# def func_1():
#     print("这⾥里里是函数1-1")
#     def func_2():
#         print("这⾥里里是函数2")
#     print("这⾥里里是函数1")
#     return func_2
# fn = func_1()   # 执⾏行行函数1.  函数1返回的是函数2, 这时fn指向的就是上⾯面函数2
# fn()     # 执⾏行行上⾯面返回的函数