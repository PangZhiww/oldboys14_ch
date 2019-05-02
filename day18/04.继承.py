# 面向对象三大特性: 继承 多台 封装
# 继承

# # class Animal:
# #     def __init__(self,name,sex,age):
# #         self.name = name
# #         self.sex = sex
# #         self.age = age
#
#
# class Person:
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
# class Cat:
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#
# class Dog:
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#
# p1 = Person("alex","laddyboy",100)


# class Animal:
#     breath = "呼吸"
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self):
#         # print(self)   # 用来验证是不是一个
#         print("动物都需要进食...")
#
#
#
# class Person(Animal):   # 括号里面的: 父类/ 基类/ 超类     括号外面的: 子类/ 派生类
#     pass
#
# class Cat:
#         pass
#
#
# class Dog:
#         pass
#
#
# p1 = Person("alex","laddyboy",100)
# print(p1.__dict__)


# 初始继承:
#   子类以及子类实例化的对象, 可以访问父类的任何方法或变量
# 类名可以访问父类所有内容
# print(Person.breath)
# Person.eat(1)
# 子类实例化的对象也可以访问父类所有内容
# p1.eat()


# print(p1)     # 用来验证是不是一个
# p1.eat()      # 用来验证是不是一个.

# 查询顺序(具体看截图)
#     先从本类中找, 找不到再从父类中找


# 练习题: 写三个类: 狗, 猫, 鸡, 每个对象都有吃, 喝    自己的方法   最后定义一个Animal类
# class Animal:
#     def __int__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#
# class Cat:
#     def eat(self):
#         print("猫吃东西")
#
#     def drink(self):
#         print("猫喝东西")
#
#
# class Dog:
#     pass
#
#
# class Chock:
#     pass


# class Animal: age
#
#     def eat(self):
#         print("%s吃东西" % (self.name))
#
#     def drink(self):
#         print("%s喝东西" % (self.name))
#
#
# class Cat(Animal):
#
#     def miaow(self)
# #
# #     def __init__(self, name, sex, age):
# #         self.name = name
# #         self.sex = sex
# #         self.age =:
#         print("喵喵叫")
# def eat(self):  # 先执行自己类中的方法, 如果没有再找父类
#     print("看这里!!!")


# class Brid(Animal):
#
#     def __init__(self, name, sex, age, wing):   # self 接收的是b1对象;    name:"鹦鹉"; sex:"公"; age:3; wing:"绿翅膀"
#
#         Animal.__init__(self, name, sex, age)
#         self.wing = wing
#
#     def bark(self):
#         print("嗷嗷叫")
#
#     def fly(self):
#         print("%s飞啊飞" % (self.wing))
#
# class Chook(Animal):
#     def crow(self):
#         print("大爷来玩啊~")


# cat1 = Cat("Tom", "公", 3)
# cat1.eat()

# 只执行父类的方法: 子类中不要定义与父类同名的方法
# 只执行子类的方法: 在子类中创建这个方法


# b1 = Brid("鹦鹉","公",3,"绿翅膀")
# b1.fly()
# print(b1.__dict__)


# 既要执行子类的方法, 又要执行父类的方法 ?
# 有两种解决方法:
#     1. Animal.__init__(self, name, sex, age)
#     2. super().__init__(name, sex, age)
#             super().父类方法名(参数(自动传self))


# class Animal:
#
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self):
#         print("%s吃东西" % (self.name))
#
#     def drink(self):
#         print("%s喝东西" % (self.name))
#
#
# class Cat(Animal):
#
#     def miaow(self):
#         print("喵喵叫")
#     # def eat(self):  # 先执行自己类中的方法, 如果没有再找父类
#     #     print("看这里!!!")
#
#
# class Brid(Animal):
#
#     def __init__(self, name, sex, age, wing):  # self 接收的是b1对象;    name:"鹦鹉"; sex:"公"; age:3; wing:"绿翅膀"
#
#         super(Brid,self).__init__(name, sex, age)
#         # super().__init__(name, sex, age)  # 简写只能在子类里面使用
#         self.wing = wing
#
#     def bark(self):
#         print("嗷嗷叫")
#
#     def fly(self):
#         print("%s飞啊飞" % (self.wing))
#
#
# class Chook(Animal):
#     def crow(self):
#         print("大爷来玩啊~")
#
#
# b1 = Brid("鹦鹉", "公", 3, "绿翅膀")
# b1.fly()
# print(b1.__dict__)


# class Animal:
#
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self):
#         print("%s吃东西" % (self.name))
#
#     def drink(self):
#         print("%s喝东西" % (self.name))
#
#
# class Cat(Animal):
#
#     def miaow(self):
#         print("喵喵叫")
#     # def eat(self):  # 先执行自己类中的方法, 如果没有再找父类
#     #     print("看这里!!!")
#
#
# class Brid(Animal):
#
#     def __init__(self, name, sex, age, wing, kaka):  # self 接收的是b1对象;    name:"鹦鹉"; sex:"公"; age:3; wing:"绿翅膀"
#
#         super(Brid, self).__init__(name, sex, age)
#         # super().__init__(name, sex, age)  # 简写只能在子类里面使用
#         self.wing = wing
#         self.kaka = kaka
#
#     def bark(self):
#         print("嗷嗷叫")
#
#     def fly(self):
#         print("%s飞啊飞" % (self.wing))
#
#     def eat(self):
#         print("%s小虫子" % (self.kaka))
#
#
# class Chook(Animal):
#     def crow(self):
#         print("大爷来玩啊~")
#
#
# b1 = Brid("鹦鹉", "公", 3, "绿翅膀","机灵")
# b1.fly()
# print(b1.__dict__)


# class Animal:
# #
# #     def __init__(self, name, sex, age):
# #         self.name = name
# #         self.sex = sex
# #         self.age = age
# #
# #     def eat(self,a1):
# #         print("%s吃%s" % (self.name,a1))
# #
# #     def drink(self):
# #         print("%s喝东西" % (self.name))
# #
# #
# # class Cat(Animal):
# #
# #     def miaow(self):
# #         print("喵喵叫")
# #     # def eat(self):  # 先执行自己类中的方法, 如果没有再找父类
# #     #     print("看这里!!!")
# #
# #
# # class Brid(Animal):
# #
# #     def __init__(self, name, sex, age, wing):  # self 接收的是b1对象;    name:"鹦鹉"; sex:"公"; age:3; wing:"绿翅膀"
# #
# #         super(Brid,self).__init__(name, sex, age)
# #         # super().__init__(name, sex, age)  # 简写只能在子类里面使用
# #         self.wing = wing
# #
# #     def bark(self):
# #         print("嗷嗷叫")
# #
# #     def fly(self):
# #         print("%s飞啊飞" % (self.wing))
# #
# #     def eat(self,cz):
# #         super().eat(cz)
# #         print("鸟吃虫子")
# #
# # class Chook(Animal):
# #     def crow(self):
# #         print("大爷来玩啊~")
# #
# #
# # b1 = Brid("鹦鹉", "公", 3, "绿翅膀")
# # b1.fly()
# # b1.eat("金蝉")
# # print(b1.__dict__)


# 继承的进阶:
# 继承: 单继承; 多继承
# 类: 经典类; 新式类

# 新式类: 凡是继承object类都是新式类
# Python3.0 所有的累都是新式类, 默认集成object.

# 经典类: 凡是不继承object类都是经典类
# Python2.0(既有新式类, 又有经典类) 所有的类默认都不继承object类, 所有的类默认都是经典类   你可以让其继承object


# 单继承: 新式类, 经典类查询顺序一样

# class  A:
#     pass
#     # def func(self):
#     #     print("IN A")
#
#
# class   B(A):
#     pass
#     # def func(self):
#     #     print("IN B")
#
# class  C(B):
#     pass
#     # def func(self):
#     #     print("IN C")
#
# c1 = C()
# c1.func()


# 多继承:
# 新式类: 遵循广度优先   广度优先查询: 每个节点有且只走一次
# 经典类: 遵循深度优先

# 多继承的新式类   广度优先: 一条路走到倒数第二级, 判断, 如果其他路能走到终点, 则返回走另外一条路. 如果不能, 则走到终点.
    # (钻石继承)


# class A:
#     def func(self):
#         print("IN A")
#
#
# class B(A):
#
#     def func(self):
#         print("IN B")
#
#
# class C(A):
#
#     def func(self):
#         print("IN C")
#
#
# class D(B):
#
#     def func(self):
#         print("IN D")
#
#
# class E(C):
#     def func(self):
#         print("IN E")
#
#
# class F(D, E):
#
#     def func(self):
#         print("IN F")
#
#
# f1 = F()
# f1.func()
# print(F.mro())  #  类名.mro() 可以查询类的继承顺序



# 多继承的经典类  深度优先: 一条路走到底