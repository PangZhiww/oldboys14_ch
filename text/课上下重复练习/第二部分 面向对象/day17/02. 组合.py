# class Count:
#     def __init__(self,name,ad,hp):
#         self.name = name
#         self.ad = ad
#         self.hp = hp
#
#     def attack(self,p):
#         p.hp = p.hp - self.ad
#         print("%s攻击%s,%s掉了%s血, 还剩%s血" % (self.name,p.name,p.name,self.ad,p.hp))
#
# p1 = Count("盖伦",50,100)
# p2 = Count("亚索",30,80)
# p1.attack(p2)


# class GameRole:
#     def __init__(self,name,ad,hp):
#         self.name = name
#         self.ad = ad
#         self.hp = hp
#     def attack(self,p):
#         p.hp = p.hp - self.ad
#         print("%s攻击%s,%s掉了%s血, 还剩%s血" %
#               (self.name, p.name, p.name, self.ad, p.hp))
#     def wea_attack(self,weaa):
#         self.weaa = weaa
#
# class Weapon:
#     def __init__(self,name,ad):
#         self.name = name
#         self.ad = ad
#     def fight(self,p1,p2):
#         p2.hp = p2.hp - self.ad
#         print("%s 用 %s 打了 %s, %s 掉了 %s 血, 还剩 %s 血"
#               % (p1.name, self.name, p2.name, p2.name, self.ad, p2.hp))
#
# p1 = GameRole("大阳哥", 20, 500)
# p2 = GameRole("印度阿宁", 50, 200)
# axe = Weapon("三板斧", 60)
# broadsword = Weapon("屠龙宝刀", 100)
#
# # print(broadsword)
# p1.wea_attack(broadsword)
# p2.wea_attack(axe)
# # .fight(p2,p1)
# # print(p1.weaa)
# p1.weaa.fight(p1,p2)
# p2.weaa.fight(p2,p1)


# class A:
#     def __init__(self, name, hp, ad):
#         self.name = name
#         self.hp = hp
#         self.ad = ad
#
#     def wae(self, wae):
#         self.wae = wae
#
#
# class B:
#     def __init__(self, name, ad):
#         self.name = name
#         self.ad = ad
#
#     def fight(self, p1, p2):
#         p2.hp = p2.hp - self.ad
#         print("%s 用 %s 打了 %s, %s 掉了 %s 血, 还剩 %s 血"
#               % (p1.name, self.name, p2.name, p2.name, self.ad, p2.hp))
#
#
# p1 = A("大阳哥", 500, 20)
# p2 = A("印度阿宁", 200, 50)
# axe = B("三板斧", 60)
# broadsword = B("屠龙宝刀", 100)
#
# p1.wae(axe)
# p1.wae.fight(p1, p2)
# p2.wae(broadsword)
# p2.wae.fight(p2,p1)