# class Animal:
#     breath = "呼吸"
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self):
#         print(self)
#         print("动物都需要进食...")
# class Persom(Animal):
#     pass
# class Cat:
#     pass
# class Dog:
#     pass
# p1 = Persom("alex","laddyboy",100)
# # print(p1.__dict__)
# Animal.eat(11)

# def func1(a1,a2):
#     print(a1)
#     print(a2)
#
# def func2(argv1,argv2,argv3):
#     print(argv1)
#     func1(argv2,argv3)
# func2(1,2,3)

# class A:
#     def func(self):
#         print("IN A")
# class B(A):
#     pass
#     # def func(self):
#     #     print("IN B")
# class C(B):
#     pass
#     # def func(self):
#     #     print("IN C")
# c1 = C()
# c1.func()

# class A:
#     def func(self):
#         print("IN A")
# class B(A):
#     # pass
#     def func(self):
#         print("IN B")
# class C(A):
#     # pass
#     def func(self):
#         print("IN C")
# class D(B):
#     # pass
#     def func(self):
#         print("IN D")
#
# class E(C):
#     # pass
#     def func(self):
#         print("IN E")
# class F(D,E):
#     # pass
#     def func(self):
#         print("IN F")
# f1 = F()
# f1.func()
# print(F.mro())

