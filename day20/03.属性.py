# class Person:
#     def __init__(self, name, hight, weight):
#         self.name = name
#         self.__hight = hight
#         self.__weight = weight
#
#     def bmi(self):
#         return "%s 的BMI值: %s" % \
#                (self.name, self.__weight / self.__hight ** 2)
#
#
# p1 = Person("Alex", 1.75, 70)
# print(p1.bmi())






# 属性
#     特点:　将一个方法，伪装成一个属性，在代码的级别上没有本质的提升，但是让其看起来很合理．
# @ 是装饰器


# 属性初始
# class Person:
#     def __init__(self, name, hight, weight):
#         self.name = name
#         self.__hight = hight
#         self.__weight = weight
#
#     @property
#     def bmi(self):
#         return "%s 的BMI值: %s" % \
#                (self.name, self.__weight / self.__hight ** 2)


# p1 = Person("Alex", 1.75, 70)
# print(p1.bmi())
# print(p1.bmi)

# 改值
# print(p1.bmi)
# p1.name = "大阳哥"
# print(p1.name)
# print(p1.bmi)





# 属性的改
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter   # 详见截图
#     def age(self,a1):
#         # print("666")
#         print(a1)
#
# p1 = Person("帅哥", 20)
# print(p1.age)
# p1.age = 26
# # print(p1.age)



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         # self.__age = age
#         if type(age) is int:
#             self.__age = age
#         else:
#             print("你输入的年龄的类型有误, 请重新输入数字")
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self,a1):
#        '''判断, 你修改的年龄必须是数字'''
#        if type(a1) is int:
#            self.__age = a1
#        else:
#            print("你输入的年龄的类型有误, 请重新输入数字")
#
#
# p1 = Person("帅哥", 20)
# # print(p1.age)
# # print(p1.__dict__)
# p1.age = 56
# # p1.age = '56'
# print(p1.age)


# property(查询): 类似于bmi这种, area, 周长....(看着是名词, 实际上是计算用property)  ***
# @age.setter(更改)   **
# @age.deleter(删除)   *
# @属性名(函数名).setter



class Person:
    def __init__(self, name, age):
        self.name = name
        # self.__age = age
        if type(age) is int:
            self.__age = age
        else:
            print("你输入的年龄的类型有误, 请重新输入数字")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,a1):
       '''判断, 你修改的年龄必须是数字'''
       if type(a1) is int:
           self.__age = a1
       else:
           print("你输入的年龄的类型有误, 请重新输入数字")

    @age.deleter
    def age(self):
        del self.__age
        # print("666")

p1 = Person("帅哥",20)
# print(p1.age)
# print(p1.__dict__)
p1.age = 56
# p1.age = '56'
print(p1.age)
del p1.age