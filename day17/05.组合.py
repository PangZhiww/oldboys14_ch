# class GameRole:
#     def __init__(self,name,ad,hp):
#         self.name = name
#         self.ad = ad
#         self.hp = hp
#
#     def attack(self,p):
#         p.hp = p.hp - self.ad
#         print("%s 攻击 %s, %s 掉了 %s 血, 还剩 %s 血" % (self.name, p.name, p.name, self.ad, p.hp))
#
# p1 = GameRole("盖伦",20,500)
# p2 = GameRole("亚索",50,200)
# p1.attack(p2)
# print(p2.hp)


# 组合:给一个类的对象封装一个属性, 这个属性是另一个类的对象


# 版本一: 添加武器: 父子, 刀, 抢, 棍, 棒...
# 代码不合理: 任务利用武器攻击别人, 你的动作发起者是人, 而不是武器
# class GameRole:
#     def __init__(self, name, ad, hp):
#         self.name = name
#         self.ad = ad
#         self.hp = hp
#
#     def attack(self, p):
#         p.hp = p.hp - self.ad
#         print("%s 攻击 %s, %s 掉了 %s 血, 还剩 %s 血" %
#               (self.name, p.name, p.name, self.ad, p.hp))
#
#
# class Weapon:
#     def __init__(self, name, ad):
#         self.name = name
#         self.ad = ad
#
#     def fight(self, p1, p2):
#         p2.hp = p2.hp - self.ad
#         print("%s 用 %s 打了 %s, %s 掉了 %s 血, 还剩 %s 血"
#               % (p1.name, self.name, p2.name, p2.name, self.ad, p2.hp))
#
# p1 = GameRole("大阳哥", 20, 500)
# p2 = GameRole("印度阿宁", 50, 200)
# axe = Weapon("三板斧", 60)
# broadsword = Weapon("屠龙宝刀", 100)
#
# axe.fight(p1,p2)
# broadsword.fight(p2,p1)


# 版本二
class GameRole:
    def __init__(self, name, ad, hp):
        self.name = name
        self.ad = ad
        self.hp = hp

    def attack(self, p):
        p.hp = p.hp - self.ad
        print("%s 攻击 %s, %s 掉了 %s 血, 还剩 %s 血" %
              (self.name, p.name, p.name, self.ad, p.hp))

    def armament_weapon(self, wea):
        self.wea = wea


class Weapon:
    def __init__(self, name, ad):
        self.name = name
        self.ad = ad

    def fight(self, p1, p2):
        p2.hp = p2.hp - self.ad
        print("%s 用 %s 打了 %s, %s 掉了 %s 血, 还剩 %s 血"
              % (p1.name, self.name, p2.name, p2.name, self.ad, p2.hp))


p1 = GameRole("大阳哥", 20, 500)
p2 = GameRole("印度阿宁", 50, 200)
axe = Weapon("三板斧", 60)
broadsword = Weapon("屠龙宝刀", 100)
# print(axe)
p1.armament_weapon(axe) # 给大阳哥 装备了三板斧这个对象,
# print(p1.wea)

# print(p1.wea.name)
# print(p1.wea.ad)

p1.wea.fight(p1,p2)