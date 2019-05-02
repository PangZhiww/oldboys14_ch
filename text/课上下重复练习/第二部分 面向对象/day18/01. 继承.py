# class A:
#     abc = "呼吸"
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#     def eat(self):
#         print("动物都要进食...")
# class B(A):
#     pass
#
# p1 = B("alex","男",187)
# print(B.abc)
# # B.eat(1)
# p1.eat()
# print(p1)


class A:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
    def eat(self):
        print("%s吃东西" % (self.name))
    def drink(self):
        print("%s喝东西" % (self.drink))
class D(A):
    def __init__(self, name, sex, age, wring, kaka):
        super().__init__(name, sex, age)
        # self.age = age
        self.wring = wring
        self.kaka = kaka
    def jiji(self):
        print("叽叽喳喳")
    # def fly(self):
    #     print("%s飞啊飞!" % (self.name))
    #
    # def eat(self):
    #     print("%s吃虫子" % (self.name))
b1 = D("鹦鹉", "公", 3, "绿翅膀", "机灵")
b1.jiji()
# print(b1.__dict__)
