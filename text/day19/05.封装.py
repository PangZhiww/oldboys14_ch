class B:
    __money = "10000"
class A(B):
    name = "alex"
    __age = 100
    # print(B.__money)
    def func(self):
        print(self.__age)
        print(A.__age)
        print("func....")
    def func1(self):
        print(self.__money)
        # print(A.money)
a1 = A()
# print(a1.name)
# print(A.name)
# a1.func()
# print(a1.__age)
# print(A.__age)
# print(A._A__age)
# print(B._B__money)


class Parent:
    def __func(self):
        print("in parent func")
    def __init__(self):
        self.__func()

class Son(Parent):
    def __func(self):
        print("in son func")

son1 = Son()