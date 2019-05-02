# class Animal:
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#     def eat(self):
#         print("%s正在吃饭ee" % (self.name))
# class Person(Animal):
#     def __init__(self,name,sex,age,pi):
#         super().__init__(name,sex,age)
#         self.pi = pi
#     def eat(self):
#         print("人类正在吃饭")
#     def pi_color(self):
#         print("黄皮肤")
# class Dog(Animal):
#     def __init__(self,color):
#         self.color = color
#     def eat(self):
#         print("狗狗正在吃饭...")
# p1 = Person("Alex","男","18","break")
# a1 = Animal("wusir","nv",96)
# p1.eat()


# class E:
#     def func(self):
#         print("IN E")
# class A(E):
#     def func(self):
#         print("IN A")
# class B:
#     def func(self):
#         print("IN B")
# class C(A):
#     # pass
#     def func(self):
#         super().func()
#         print("IN C")
# c1 = C()
# c1.func()

# class Parent:
#     def func(self):
#         print("in Parent func")
#     def __init__(self):
#         self.func()
# class Son(Parent):
#     def func(self):
#         print("in Son func")
# sonl = Son()
# son1.func()

# class A:
#     name = []
# p1 = A()
# p2 = A()
# p1.name.append(1)
# p1.age = 12
#
# print(p2.name)

# class A:
#     name = "alex"
# p1 = A()
# p2 = A()
# p2.name = "wusir"
# print(p1.name)
# print(p2.name)
# print(A.name)

class A:
    def func(self):
        print("IN A")
class B(A):
    def func(self):
        print("IN B")
class C(A):
    def func(self):
        print("IN C")
class D(B):
    def func(self):
        print("IN B")
class E(C):
    def func(self):
        print("IN E")
class F(D,E,B):
    def func(self):
        print("IN F")

f1 = F()
f1.func()
print(F.mro())