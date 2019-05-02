# Python面向对象的三大特征:
# 多态(多种形态): Python处处是多态
# Java: 强类型语言
# int i = 666
# i = "alex"  # 报错

# def func(list,a):
#     print(a)


class Fox():
    pass
    # print("nb")


class Whitebone():
    pass


obj1 = Fox()
obj2 = Whitebone()


class Monkey():
    def fight(self):
        pass


Monkey.fight(obj1)


# python: 弱类型语言

# python 不管什么类型, 传入函数, 封装到对象中都可以

# Python 没有多态? 他有什么? 她有鸭子类型
# 鸭子类型: 看着像鸭子, 他就是鸭子

# 这些类, 都互称为鸭子    类中含有相同的方法
    # 多各类中有相同的方法, 那么这些类就互称为鸭子
class Str:
    def index(self):
        pass


class List:
    def index(self):
        pass


class Tuple:
    def index(self):
        pass
