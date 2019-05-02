# class Person:
#     animal = "高级动物"
#     soup = "有灵魂的"
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
#         print("%s在吃饭..." % (self.name))
#
#     def sleep(self):
#         pass
#
#     def work(self):
#         pass
#
#
# ret1 = Person("中国", "alex", "未知", 42, 175)
# ret2 = Person("美国", "武大", "男", 35, 160)
# ret3 = Person("哥本哈根", "太白", "女", 54, 170)
# ret4 = Person("中国", "武大", "女", 35, 170)
# ret1.eat()
# ret2.eat()
# ret3.eat()
# print(ret1.animal)
# print(ret2.soup)
# print(Person.__dict__["language"])


# class Person:
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def w1(self):
#         print("%s，%s岁，%s，上山去砍柴" % (self.name,self.age,self.sex))
#     def w2(self):
#         print("%s，%s岁，%s，开车去东北" % (self.name,self.age,self.sex))
#     def w3(self):
#         print("%s，%s岁，%s，最爱大保健" % (self.name,self.age,self.sex))
# r1 = Person("小明",10,"男")
# r2 = Person("老李",90,"男")
#
# r1.w1()
# r1.w2()
# r1.w3()
# r2.w1()
# r2.w2()
# r2.w3()

# class Game_role:
#     def __init__(self,name,ad,hp):
#         self.name = name
#         self.ad = ad
#         self.hp = hp
#     def fight(self,p1):
#         p1.hp = p1.hp - self.ad
#         print("%s攻击%s,%s掉了%s滴血, 还剩%s" %
#               (self.name,p1.name,p1.name,self.ad,p1.hp))
#
# p1 = Game_role("盖伦",10,100)
# p2 = Game_role("剑豪",20,80)
# p1.fight(p2)
