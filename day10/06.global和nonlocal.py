
# a = 10
# def func():
#     # a = 20    # 在自己的作用域中使用的a, 是全新的变量a
#     global a    # 把外面全局中的a引入
#     a = a + 1
#     print(a)
# func()
# print(a)


a = 10
def func():
    # a = 20    # 在自己的作用域中使用的a, 是全新的变量a
    global a    # 把外面全局中的a引入
    a = 30      # 修改赋值
    print(a)
func()
print(a)



# a = 1
# def fun_1():
#     a = 2
#     def fun_2():
#         nonlocal a
#         a = 3
#         def fun_3():
#             a = 4
#             print(a)
#         print(a)
#         fun_3()
#         print(a)
#     print(a)
#     fun_2()
#     print(a)
# print(a)
# fun_1()
# print(a)


# a = 1
# def fun_1():
#     a = 2
#     def fun_2():
#         def fun_3():
#             nonlocal a
#             a = 4
#             print(a)
#         print(a)
#         fun_3()
#         print(a)
#     print(a)
#     fun_2()
#     print(a)
# print(a)
# fun_1()
# print(a)

