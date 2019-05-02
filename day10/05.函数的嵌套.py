# def func1():
#     print("哈哈")
#
# def func2():
#     func1()
#     print("呵呵")
#     func2()
#
# func2()     # 998次循环


# def func1():
#     print("呵呵")
#     def func2():
#         print("哈哈")
#     func2()
#     print("吼吼")
#
# func1()


# def func1():
#     print("赵")
#     def func2():
#         print("钱")
#         def func3():
#             print("孙")
#         print("李")
#         func3()
#     print("周")
#     func2()
# func1()


def func1():
    print("赵")
    def func2():
        print("钱")
        def func3():
            print("孙")
        print("李")
    def func4():
        print("哈哈")
        func2()
    print("周")
    func2()
func1()

