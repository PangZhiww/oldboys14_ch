# def func():
#     print('我是周杰伦')
#     yield '昆凌'      # 函数中包含了 yield, 当前这个函数就不再是普通函数了.  是生成器函数
#     print('我是王力宏')
#     yield '我是李云迪???'
#     print('我是笛卡尔积')
#     yield '笛卡尔积是谁'
#     # print('你好啊')    # 最后一个 yield 之后如果再进行 __next__() 会报错
#
# g = func()  # 通过函数 func() 来创建一个生成器
# print(g.__next__()) # 周杰伦
# print(g.__next__()) # 王力宏
# print(g.__next__()) # 笛卡尔积
# print(g.__next__())
# print(g.__next__())

# return 直接返回结果, 结束函数的调用
# yield 返回结果, 可以让函数分段执行

# g1 = func()
# g2 = func()
# print(g1.__next__())
# print(g1.__next__())
# print('===================')
# print(g2.__next__())
# print(g2.__next__())


# def func():
#     lst = []
#     for i in range(1,1000):
#         lst.append('衣服%s' % i)
#     return lst
# print(func())


# def gen():  # 颜涛老师的方法
#     i = 1
#     while i < 1001:
#         yield "衣服%s" % i
#         i = i+1
# s = gen()

# def func():
#     for i in range(1,100):
#         yield '衣服%s' % i

# s = func()
# print(s.__next__())
# print(s.__next__())
# print(s.__next__())
# print(s.__next__())


def func():
    yield 11
    yield 22
    yield 33
    yield 44
    yield 55

f = func()    # 拿到的是生成器. 生成器的本质是迭代器. 迭代器可以被迭代 生成器可以直接for循环

# it = f.__iter__()
# while 1:
#     try:
#         print(it.__next__())
#     except StopIteration:
#         break

# for i in f:
#     print(i)
print(list(f))