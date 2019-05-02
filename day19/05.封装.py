# 广义的封装: 实例化一个对象, 给对象空间封装一些属性
# 狭义的封装: 私有制
# 私有成员: 私有静态字段, 私有方法, 私有对象属性

# 私有静态字段
# class B:
#     __money = 1000000
#
#
# class A(B):
#     name = "alex"
#     __age = 188
#
#     def func(self):
#         print(self.__age)
#         print(A.__age)    # 对于私有静态字段, 累的内部可以访问
#         print("func...")    # 对于私有静态字段, 累的内部可以访问
#
#     def func1(self):
#         print(self.__money)
#         print(A.__money)
#
# a1 = A()
# print(a1.name)
# print(A.name)
# print(a1.__age)   # 实例化对象不能访问私有静态字段(调用)
# print(A.__age)   # 类名不能访问私有静态字段
# 对于私有静态字段, 类的外部不能访问.

# a1.func()   # 对于私有静态字段, 累的内部可以访问
# a1.func1()  # 对于私有静态字段来说, 只能在本类中内部访问, 类的外部, 派生类(子类)均不可访问

# 可以访问, 但是工作中千万不要用
# print(A._A__age)
# print(A._B__money)
# print(B.__dict__)


# 私有方法

class B:
    __money = 1000000


class A(B):
    name = "alex"
    __age = 188

    def func(self):
        print(self.__age)
        print(A.__age)    # 对于私有静态字段, 累的内部可以访问
        print("func...")    # 对于私有静态字段, 累的内部可以访问

    def func1(self):
        print(self.__money)
        print(A.__money)

a1 = A()