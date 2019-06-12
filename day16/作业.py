# class Person:
#     animal = '高级动物'
#     soul = '有灵魂'
#     language = "语言"
#
#     def __init__(self, country, name, sex, age, hight):
#         self.country = country
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.hight = hight
#
#     def eat(self):
#         print("%s最喜欢吃饭" % self.name)
#
#     def sleep(self):
#         print("%s都喜欢睡觉" % self.sex)
#
#     def work(self):
#         print("我们都爱工作")
#
#
# ret1 = Person('中国', 'alex', '男', '18', '167')
# ret2 = Person('美国', 'wuse', '女', '38', '197')
# ret3 = Person('Japen', 'taibai', '男', '18', '152')
# ret4 = Person(ret1.country,ret2.name,ret3.sex,ret2.age,ret3.hight)

# print(ret1.__dict__)
# print(ret2.__dict__)
# print(ret3.__dict__)
# print(ret4.__dict__)

# ret1.eat()
# ret2.eat()
# ret3.eat()
# ret4.eat()
#
# ret1.sleep()


# print(ret1.animal)

# print(Person.__dict__)






# class HappuDay:
#
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def Chopwood(self):
#         print("%s上山去勘察" % self.name)
#
#     def Drive(self):
#         print("%s开车去东北" % self.name)
#
#     def Great(self):
#         print("%s最爱大保健" % self.name)
#
# p1 = HappuDay("小明",10,"男")
#
# p1.Drive()