class A:
    def __init__(self, name, sex, age, ad, hp):
        self.name = name
        self.sex = sex
        self.age = age
        self.ad = ad
        self.hp = hp

    def add_moto(self, mo):
        self.mo = mo

    def fight(self, a):
        a.hp = a.hp - self.ad
        print("%s赤手空拳打了%s的%s滴血, %s还剩%s血." %
              (self.name, a.name, self.ad, a.name, a.hp))

    def add_fight(self, bb):
        self.bb = bb

    def all(self, p):
        p.hp = p.hp - self.bb.ad
        # print("%s骑着%s打了骑着%s的%s一%s, %s哭了, 还剩%s滴血." %
        #       (self.name,self.mo.name,p.mo.name,p.name,self.bb.name,p.name,p.hp))
        print("{0}骑着{1}打了骑着{2}的{3}一{4}, {3}哭了, 还剩{5}滴血.".format
              (self.name, self.mo.name, p.mo.name, p.name, self.bb.name, p.hp))


class B:
    def __init__(self, name, ad):
        self.name = name
        self.ad = ad

    def axe(self, a):
        a.hp = a.hp - self.bb.ad
        print("%s利用%s打了%s一%s, %s还剩%s血." %
              (self.name, self.bb.name, a.name, self.bb.name, a.name, a.hp))


class C:
    def __init__(self, name, sp):
        self.name = name
        self.sp = sp

    def moto(self):
        print("%s骑着%s开着%s迈的车行驶在赛道上." %
              (a3.name, self.name, self.sp))


a1 = A("苍井井", "女", 18, 20, 200)
a2 = A("东尼木木", "男", 28, 30, 150)
a3 = A("波多多", "女", 19, 50, 80)

b1 = B("平底锅", 20)
b2 = B("斧子", 50)
b3 = B("双节棍", 65)

c1 = C("小踏板", 60)
c2 = C("雅马哈", 80)
c3 = C("宝马", 120)

# a1.add_moto(c1)
# a1.mo.moto(a1)
# a2.add_moto(c2)
# a2.mo.moto()
# a3.add_moto(c3)
# a3.mo.moto()


# a1.fight(a2)
# a2.fight(a3)


# a1.add_fight(b1)
# a1.bb.axe(a3,a1)
# a2.add_fight(b2)
# a2.bb.axe(a3,a1)


# a1.add_moto(c1)
# a1.add_fight(b3)
# a2.add_moto(c3)
# a1.all(a2)

# a2.add_moto(c3)
# a2.add_fight(b3)
# a3.add_moto(c1)
# a2.all(a3)

# 完善代码
a1.add_fight(b2)
a1.bb.axe(a2)