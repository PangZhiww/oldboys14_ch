# 第一题
#
# class Animal:
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self):
#         print("%s正在吃饭" % (self.name))
#
# class Person(Animal):
#     def __init__(self,name,sex,age,skin):
#         super().__init__(name,sex,age)
#         self.skin = skin
#
#     def eat(self):
#         print("人类正在吃饭")
#
# class Dog(Animal):
#     def __init__(self,name,sex,age,coat_color):
#         super().__init__(name,sex,age)
#         self.coat_color = coat_color
#
#     def eat(self):
#         super().eat()
#         print("狗狗正在吃饭")

# p1 = Person("黄皮肤")
# p1.skin()

# p2 = Person("李富贵","男",18,"黄皮肤")
# print(p2.__dict__)
#
# p4 = Dog("alex","母",3,"黑毛")
# print(p4.__dict__)




# 第二题

# class A:
#     def func(self):
#         print("in A")
#
#
# class B:
#     def func(self):
#         print("IN B")
#
#
# class C(A, B):
#     def func(self):
#         print("IN C")
#
# c1 = C()
# c1.func()

# 1. 让其执行C类中的func

# class A:
#     def func(self):
#         print("in A")
#
#
# class B:
#     def func(self):
#         print("IN B")
#
#
# class C(A, B):
#     def func(self):
#         print("IN C")
#
# c1 = C()
# c1.func()

# 2. 让其执行A类中的func
#
# class A:

#     def func(self):
#         print("in A")
#
# class B:
#     def func(self):
#         print("IN B")
#
# class C(A,B):
#     pass

# c1 = C()
# c1.func()


# 3. 让其执行B类中的func

# class A:
#     pass
#
# class B:
#     def func(self):
#         print("IN B")
#
# class C(A,B):
#     pass
#
# c1 = C()
# c1.func()

# 4. 让其既执行C类的func, 又执行A类中的func

# class A:
#     def func(self):
#         print("IN A")
#
# class B:
#     def func(self):
#         print("IN B")
#
# class C(A,B):
#     def func(self):
#         super().func()
#         print("IN C")
#
# c1 = C()
# c1.func()

# 5. 让其既执行C类中的func, 又执行B类中的func
# class A:
#     pass
#     # def func(self):
#     #     print("IN A")
#
# class B:
#     def func(self):
#         print("IN B")
#
# class C(A,B):
#     def func(self):
#         super().func()
#         print("IN C")
#
# c1 = C()
# c1.func()




# 第三题

# class Parent:
#     def func(self):
#         print("in Parent func")
#
#     def __init__(self):
#         self.func()
#
# class Son(Parent):
#     def func(self):
#         print("in Son func")
#
# son1 = Son()          # 详见截图



# 第四题
class A:
    name = []

p1 = A()
p2 = A()

p1.name.append(1)
# p1.name, p2.name, A.name 分别是什么 ?

print(p1.name)
print(p2.name)
print(A.name)


# p1.age = 12
# p1.age, p2.age, A.age 分别又是什么?  为什么?

# print(p1.age)
# print(p2.age)
# print(A.age)