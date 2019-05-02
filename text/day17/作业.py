# class Person:
#     def __init__(self, name, sex, age, ad, hp):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.ad = ad
#         self.hp = hp
#
#     def vechicle_add(self, c_speed):
#         self.c_speed = c_speed
#
#     def ko_person(self, person_hp):
#         person_hp.hp = person_hp.hp - self.ad
#         print("%s赤手空拳打了%s%s滴血，波多多还剩%s血"
#               % (self.name, person_hp.name, self.ad, person_hp.hp))
#
#     def fight_add(self, koo):
#         self.koo = koo
#
#     def moc(self, p2):
#         p2.hp = p2.hp - self.ad - self.koo.ad
#         print("{0}骑着{1}打了骑着{2}的{3}一{4}，{3}哭了，还剩{5}血".format
#               (self.name, self.c_speed.name, p2.c_speed.name, p2.name, self.koo.name, p2.hp))


# class Vehicle:
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed
#
#     def cycling(self, r1):
#         print("%s骑着%s开着%s迈的车行驶在赛道上。" %
#               (r1.name, self.name, self.speed))
#
#
# class Fight:
#     def __init__(self, name, ad):
#         self.name = name
#         self.ad = ad
#
#     def tool_koo(self, pp1, pp2):
#         pp2.hp = pp2.hp - self.ad - pp1.ad
#         print("%s利用%s打了%s一%s，%s还剩%s血。" %
#               (pp1.name, self.name, pp2.name, self.name, pp2.name, pp2.hp))
#
#
# p1 = Person("苍井井", "女", 18, 20, 200)
# p2 = Person("东尼木木", "男", 20, 30, 150)
# p3 = Person("波多多", "女", 19, 50, 80)
# #
# w1 = Fight("平底锅", 20)
# w2 = Fight("斧子", 50)
# w3 = Fight("双节棍", 65)
# c1 = Vehicle("小踏板", 60)
# c2 = Vehicle("雅马哈", 80)
# c3 = Vehicle("宝马", 120)
# p1.vechicle_add(c1)
# p1.c_speed.cycling(p1)
# p2.vechicle_add(c3)
# p2.c_speed.cycling(p2)
# p3.vechicle_add(c2)
# p3.c_speed.cycling(p3)
# p1.ko_person(p3)
# p2.ko_person(p3)
# p1.fight_add(w1)
# p1.koo.tool_koo(p1,p2)
# p3.fight_add(w1)
# p3.koo.tool_koo(p3,p1)
# p3.fight_add(w2)
# p3.koo.tool_koo(p3,p2)
# p1.vechicle_add(c3)
# p1.fight_add(w3)
# p2.vechicle_add(c1)
# p1.moc(p2)

# p3.vechicle_add(c1)
# p3.fight_add(w2)
# p2.vechicle_add(c2)
# p3.moc(p2)

# from math import pi
# li = int(input("请输入半径: "))
# class Circle:
#     def __init__(self,r):
#         self.r = r
#     def area(self):
#         return round(self.r ** 2 * pi,2)
#     def perimerter(self):
#         return round(self.r * 2 * pi,2)
#
# c1 = Circle(li)
# print(c1.area())
# print(c1.perimerter())

# goods = ["1","骑车","飞机","大炮"]
# for i in range(1,len(goods)):
#     print(i,goods[i])
# num = input("请输入要选择的序号:")
# num = int(num)
# text = "您选择的是 %s "% (goods[num],)
# print(text)

# from math import pi
# class Ring:
#     def __init__(self,r1,r2):
#         self.r1 = r1
#         self.r2 = r2
#
#     def area(self):
#         return round(self.r1 ** 2 * pi - self.r2 ** 2 * pi,2)
#     def perimeter(self):
#         return round(self.r1 * 2 * pi + self.r2 * 2 * pi, 2)
# r1 = Ring(6,3)
# print(r1.area())
# print(r1.perimeter())

# from math import pi
# class Ring:
#     def __init__(self,r1,r2):
#         self.r1 = Crcle(r1)
#         self.r2 = Crcle(r2)