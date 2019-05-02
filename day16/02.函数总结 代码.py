# def func(*args,**kwargs):
#     print(args)
# print(kwargs)

# 当定义一个函数的时候: * 代表 聚合
# 当执行一个函数的时候: * 代表 打散

# func(1,2,3,name='alex',agr=100)

# l1 = [1,2,3]
# l2 = [4,5,6]
# func(*l1,*l2)
# func(*l1)   # args = (1,2,3) == print(1,2,3)    print可以直接接收*args    但是不能接收**kwargs


# def func1():
#     a = 1
#     b = 2
#     print(a)
#
#     def func2():
#         b = 3
#         print(b)
#
#     print(666)
#     func2()
#     print(111)
#
# func1()

# def func1():
#     a = 1
#     b = 2
#     print(a)
#
#     def func2():
#         b = 3
#         print(b)
#
#     print(666)
#     return func2
#
#
# func1()()



# l1 = [i for i in range(1,100)]
# l1 = [i for i in range(1,100) if i > 50]
# l1 = [i for i in range(1,100) if i > 50]