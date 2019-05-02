class GameRole:
    def __init__(self, name, sex, age, ad, hp):
        self.name = name
        self.sex = sex
        self.age = age
        self.ad = ad
        self.hp = hp

    def attack(self, p):
        p.hp = p.hp - self.ad
        print("%s赤手空拳打了%s%s滴血, %s还剩%s滴血" %
              (self.name, p.name, self.ad, p.name, p.hp))

    def add_moto(self, mo):
        self.mo = mo

    def add_weapon(self, wee):
        self.wee = wee

    def road_rush(self, p1):
        p1.hp = p1.hp - self.wee.ad
        print("%s骑着%s打了骑着%s的%s一%s, %s哭了, 还剩%s血." %
              (self.name, self.mo.name, p1.mo.name, p1.name, self.wee.name, p1.name, p1.hp))


class Weapon:
    def __init__(self, name, ad):
        self.name = name
        self.ad = ad

    def fight(self, p1, p2):
        p2.hp = p2.hp - self.ad
        print("%s利用%s打了%s一%s, %s还剩%s血."
              % (p1.name, self.name, p2.name, self.name, p2.name, p2.hp))


class Moto:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def drive(self, p1):
        print("%s骑着%s开着%s迈的车行驶在赛道上" %
              (p1.name, self.name, self.speed))


p1 = GameRole("alex", "男", 52, 30, 100)
p2 = GameRole("太白", "女", 22, 20, 110)
p3 = GameRole("邱彦涛", "男", 55, 50, 70)

w1 = Weapon("平底锅", 10)
w2 = Weapon("小匕首", 20)

m1 = Moto("小绵羊", 30)
m2 = Moto("助力车", 20)
m3 = Moto("丰田", 50)

# (1) 苍井井骑着小踏板开着60迈的车行驶在赛道上.
# (2) 东尼木木骑着宝马开着120迈的车行驶在赛道上.
# (3) 波多多骑着雅马哈开着80迈的车行驶在赛道上
# p1.add_moto(m1)
# p1.mo.drive(p1)
#
# p2.add_moto(m2)
# p2.mo.drive(p2)
#
# p3.add_moto(m3)
# p3.mo.drive(p3)

# (4) 苍井井赤手空拳打了波多多的20滴血, 波多多还剩xx血.
# (5) 东尼木木赤手空拳打了波多多30滴血, 波多多还剩xx血.
# p1.attack(p2)
# p2.attack(p3)

# (6) 波多多利用平底锅打了苍井井一平底锅, 苍井井还剩xx血.
# (7) 波多多利用斧子打了东尼木木一斧子, 东尼木木还剩xx血.
# p1.add_weapon(w1)
# p1.we.fight(p1,p2)
#
# p2.add_weapon(w2)
# p2.we.fight(p2,p3)

# (8) 苍井井骑着宝马打了骑着小踏板的东尼木木一双截棍, 东尼木木哭了, 还剩xx血.
# (9) 波多多骑着小踏板打了骑着雅马哈的东尼木木一斧子, 东尼木木哭了, 还剩xx血.
# p1.add_moto(m1)
# p1.add_weapon(w1)
# p2.add_moto(m2)
# p1.road_rush(p2)
