# 类方法
# class A:
#     def func(self):     # 普通方法
#         print(self)
#
#     @classmethod    # 类方法   不用传参数
#     def func1(cls):
#         print(cls)

# a1 = A()
# a1.func()
# A.func(a1)      # a1 = A()    a1.func == A.func(a1)


# 类方法:　通过类名调用的方法，类方法种第一个参数的约定俗称 cls, Python自动将类名(类空间)传给cls
# A.func1()   # 类方法   不用传参数
#
# a1 = A()
# a1.func1()  # 对象调用类方法, cls 得到的是类本身



# 类方法应用场景:
#   1. 类中有些方法是不需要对象参与.
#   2. 对类中的静态变量进行改变, 要用到类方法
#   3. 继承中, 父类得到子类的类空间       (在父类中的类方法得到子类的类空间, 为所欲为)


# class A:
#     name = "alex"
#     count = 1
#
#     def func1(self):    # 此方法无需对象参与
#         return A.name + str(A.count + 1)
#
# A.func1(111)    # 不可取
# a1 = A()
# print(A.func1(a1))



# 情况一:
# class A:
#     name = "alex"
#     count = 1
#
#     @classmethod    # 类方法   不用传参数
#     def func1(cls):
#         return A.name + str(A.count + 1)
#
# print(A.func1())


# 情况一改进:
# class A:
#     name = "alex"
#     count = 1
#
#     @classmethod    # 类方法   不用传参数
#     def func1(cls):
#         return cls.name+ str(cls.count + 1)
#
# print(A.func1())



# 情况二:
# class A1:
#     name = "alex"
#     count = 1
#
#     @classmethod    # 类方法   不用传参数
#     def func1(cls):
#         return cls.name+ str(cls.count + 1)



# 情况三:
#   可以查询和更改子类空间的所有东西, 但是不能查询对象属性   可以得到子类空间的任意值
# class A:
#     # name = "alex"
#     # count = 1
#     age = 12
#
#     @classmethod    # 类方法   不用传参数
#     def func1(cls):
#         # print(cls)
#         # 对 B 类的所有内容可以进行修改
#         print(cls.age)
#         # return cls.name+ str(cls.count + 1)
#
# class B(A):
#     # def f1(self):
#     #     pass
#
#     age = 22
#
# B.func1()




# 不通过类方法, 想让我的父类的某个方法得到子类的空间里面的任意值
    # 只能查询子类空间的所有东西, 但不可以更改, 可以查类方法,还可以查对象里面的属性    可以得到子类空间的任意值
# class A:
#     age = 12
#
#     @classmethod    # 类方法   不用传参数
#     def func1(cls):
#         # 对 B 类的所有内容可以进行修改
#         print(cls.age)
#
#     def func2(self):
#         print(self)     # self 子类的对象, 能得到子类空间的任意值
#
# class B(A):
#     age = 22
#
# # B.func1()
# b1 = B()
# b1.func2()



# 静态变量:
# class A:
#     @staticmethod     # 静态方法
#     def func():
#         print(666)
#
# A.func()

# def login(username,password):
#     if username == "alex" and password == 123:
#         print("登陆成功")
#     else:
#         print("登陆失败...")
#
# login("alex", 123)


class A:
    @staticmethod
    def login(username, password):
        if username == "alex" and password == 123:
            print("登陆成功!!!")
        else:
            print("登陆失败...")

A.login("alex", 123)


# 1. 代码块, 清晰
# 2. 复用性