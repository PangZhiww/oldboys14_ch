# name = 'wusir'   # 变量写在全局是不安全的
#
# def abc():
#     global name
#     name = '呵呵'
# abc()



# def func():
#     name = 'alex'   # 闭包作用: 常驻内存  防止其他程序改变这个变量
#     def inner():
#         print(name)     # 在内层函数中调用了外层函数的变量, 叫闭包. 可以让一个局部变量常驻内存
#     return inner
#
# ret = func()
# ret()   # 执行的是inner
# ret()
# ret()
# ret()
# ret()
# ret()



# 闭包的好处
# from urllib.request import urlopen
# def but():
#     content = urlopen('http://www.h3c.com/cn/').read
#     def inner():
#         return content    # 在函数内部使用了外部的变量. 闭包
#     # print(inner.__closure__)    # 查看inner是否是闭包, 如果有东西就是闭包, 返回None没东西就不是闭包
#     return inner
# print('加载中.......')
# print(but()())

# fn = but()      # 这个时候就开始夹在网址的内容了
# # 后面需要用到这里面的内容就不需要子再执行 非常耗时的网络连接操作了
# content = fn()  # 获取内容
# print(content)
# content2 = fn()   # 重新获取内容
# print(content2)



# def func1():
#     name = "alex"
#     def func2():
#         print(name)     # 闭包
#     func2()
#     print(func2.__closure__)    # (<cell at 0x10c2e20a8: str object at 0x10c3fc650>,)
# func1()