# g = (i for i in range(10))
# print(g)
#
# for e in g:
#     print(e)
#
# print(list(g))


# gen = ('马化腾我第%s次爱你' % i for i in range(10))
# for i in gen:
#     print(i)



def func():
    print('111')
    yield '222'

g = func()  # 生成器g
g1 = (i for i in g)     # 生成器g1. 但是g1的数据来源于g
g2 = (i for i in g1)    # 生成器g2.  来源于g1

print(list(g))    # 获取g中的数据. 这时func()才会被执⾏行行. 打印111.获取到222. g完毕.
print(list(g1))     # 获取g1中的数据. g1的数据来源是g. 但是g已经取完了了. g1 也就没有数据 了了
print(list(g2))
# for i in g2:
#     print(list(i))