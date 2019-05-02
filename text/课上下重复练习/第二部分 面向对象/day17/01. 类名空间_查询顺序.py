# class Person:
#     animal = "高级动物"
#     soul = "有灵魂的"
#     language = "语言"
#
#     def __init__(self,country,name,sex,age,hight):
#         self.country = country
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.hight = hight
#
#     def eat(self):
#         print("%s吃饭" % self.name)
#     def sleep(self):
#         print("睡觉")
#     def work(self):
#         print("工作")
#
# p1 = Person("菲律宾","alex","未知",42,175)
# p2 = Person("美国","武大","男",42,175)
# p3 = Person("中国","太白","女",42,175)
# p4 = Person(p1.country,p2.name,p2.sex,p1.age,p2.hight)
#
# # p1.wight = 150
# # p1.eat()
# print(p4.__dict__)


class Count:
    count = 0
    def __init__(self):
        Count.count = Count.count + 1

obj1 = Count()
obj1 = Count()
obj1 = Count()
obj1 = Count()
obj1 = Count()
obj1 = Count()

Count.count = 6
print(Count.__dict__)
print(Count.count)
# count = 0
# def func():
#     print(count)
# func()