class GameRole:
    def __init__(self,name,ad,hp):
        self.name = name
        self.ad = ad
        self.hp = hp
    def attack(self,p):
        p.hp = p.hp - self.ad
        print('%s 攻击 %s,%s 掉了%s血,还剩%s血' %
              (self.name,p.name,p.name,self.ad,p.hp))
    def armament_weapon(self,wea):
        self.wea = wea
class Weapon:
    def __init__(self,name,ad):
        self.name = name
        self.ad = ad
    def fihght(self,p1,p2):
        p2.hp = p2.hp - self.ad
        print('%s 用%s打了%s,%s 掉了%s血,还剩%s血' %
              (p1.name,self.name,p2.name,p2.name,self.ad,p2.hp))

p1 = GameRole('大阳哥',20,500)
p2 = GameRole('印度阿宁',50,200)
axe = Weapon('三板斧',60)
broadsword = Weapon('屠龙宝刀',100)

p1.armament_weapon(axe)
p1.wea.fihght(p1,p2)