# 1,完成下列功能:
#   1.1创建一个人类Person,再类中创建3个静态变量(静态字段)
#     animal = '高级动物'
#     soup = '有灵魂'
#     language = '语言'
#   1.2在类中定义三个方法,吃饭,睡觉,工作.
#   1.3在此类中的__init__方法中,给对象封装5个属性:国家,姓名,性别,年龄,  身高.
#   1.4实例化四个人类对象:
#     第一个人类对象p1属性为:中国,alex,未知,42,175.
#     第二个人类对象p2属性为:美国,武大,男,35,160.
#     第三个人类对象p3属性为:你自己定义.
#     第四个人类对象p4属性为:p1的国籍,p2的名字,p3的性别,p2的年龄,p3  的身高.
#   1.5 通过p1对象执行吃饭方法,方法里面打印:alex在吃饭.
#   1.6 通过p2对象执行吃饭方法,方法里面打印:武大在吃饭.
#   1.7 通过p3对象执行吃饭方法,方法里面打印:(p3对象自己的名字)在吃饭.
#   1.8 通过p1对象找到Person的静态变量 animal
#   1.9 通过p2对象找到Person的静态变量 soul
#   2.0 通过p3对象找到Person的静态变量 language
#
# 2,通过自己创建类,实例化对象
#   在终端输出如下信息
#   小明，10岁，男，上山去砍柴
#   小明，10岁，男，开车去东北
#   小明，10岁，男，最爱大保健
#   老李，90岁，男，上山去砍柴
#   老李，90岁，男，开车去东北
#   老李，90岁，男，最爱大保健
#   老张…
#
# 3,模拟英雄联盟写一个游戏人物的类（升级题）.
#   要求:
#   (1)创建一个 Game_role的类.
#   (2) 构造方法中给对象封装name,ad(攻击力),hp(血量).三个属性.
#   (3) 创建一个attack方法,此方法是实例化两个对象,互相攻击的功能:
#       例: 实例化一个对象 盖伦,ad为10, hp为100
#       实例化另个一个对象 剑豪 ad为20, hp为80
#       盖伦通过attack方法攻击剑豪,此方法要完成 '谁攻击谁,谁掉了多少血,  还剩多少血'的提示功能.



# class Person:
#     animal = "高级动物"
#     soup = "有灵魂"
#     language = "语言"
#
#     def eat(self):
#         print("%s在吃饭" % self.name)
#     def sleep(self):
#         pass
#     def wrok(self):
#         pass
#     def __init__(self,country,name,sex,age,hight):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.hight = hight
#
# ret1 = Person("中国","alex","男",86,153)
# ret2 = Person("美国","武大","女",35,189)
# ret3 = Person("日本","太白","女",16,"555")
# ret4 = Person("中国","武大","男",35,"186")

# ret1.eat()
# ret2.eat()
# ret3.eat()
# print(ret1.animal)
# print(ret1.soup)
# print(ret1.language)



# 2,通过自己创建类,实例化对象
#   在终端输出如下信息
#   小明，10岁，男，上山去砍柴
#   小明，10岁，男，开车去东北
#   小明，10岁，男，最爱大保健
#   老李，90岁，男，上山去砍柴
#   老李，90岁，男，开车去东北
#   老李，90岁，男，最爱大保健
#   老张…


# class Pronse:
#     def __init__(self,name,age,sex,going):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.going = going
#     def work(self):
#         print("%s,%s岁,%s,%s" % (self.name,self.age,self.sex,self.going))
# p1 = Pronse("小明",10,"男","上山去砍柴")
# p2 = Pronse("小明",10,"男","开车去东北")
# p3 = Pronse("小明",10,"男","最爱大保健")
# p4 = Pronse("老李",90,"男","上山去砍柴")
# p5 = Pronse("老李",90,"男","开车去东北")
# p6 = Pronse("老李",90,"男","最爱大保健")
#
# p1.work()
# p2.work()
# p3.work()
# p4.work()
# p5.work()
# p6.work()



# 3,模拟英雄联盟写一个游戏人物的类（升级题）.
#   要求:
#   (1)创建一个 Game_role的类.
#   (2) 构造方法中给对象封装name,ad(攻击力),hp(血量).三个属性.
#   (3) 创建一个attack方法,此方法是实例化两个对象,互相攻击的功能:
#       例: 实例化一个对象 盖伦,ad为10, hp为100
#       实例化另个一个对象 剑豪 ad为20, hp为80
#       盖伦通过attack方法攻击剑豪,此方法要完成 '谁攻击谁,谁掉了多少血,  还剩多少血'的提示功能.

# class Game_role:
#     def __init__(self,name,ad,hp):
#         self.name = name
#         self.ad = ad
#         self.hp = hp
#
#     def attack(self,a1):
#         a1.hp = a1.hp - self.ad
#         print("%s攻击%s,%s掉了%s血,  还剩%s血" % (self.name,a1.name,a1.name,self.ad,a1.hp))
#
# a1 = Game_role("盖伦",10,100)
# a2 = Game_role("剑豪",20,80)
# a1.attack(a2)