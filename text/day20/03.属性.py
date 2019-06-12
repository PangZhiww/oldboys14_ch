# class Person:
#     def __init__(self,name,hight,weight):
#         self.name = name
#         self.__hight = hight
#         self.__weight = weight
#     @property
#     def bmi(self):
#         return '%s 的bmi 值%s' %\
#                (self.name,self.__weight / self.__hight ** 2)
# p1 = Person('大阳哥',1.68,70)
# # print(p1.name)
# # print(p1.__dict__)
# print(p1.bmi)
# p1.name = "alex"
# print(p1.name)
# print(p1.bmi)

