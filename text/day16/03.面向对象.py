# s1 = "fasajod"
# count = 1
# for i in s1:
#     count = count + 1
#     print(count)
# print(count)

# l1 = [1,2,3]
# count = 0
# for i in l1:
#     count = count + 1
# print(count)

# def my_len(argy):
#     count = 0
#     for i in argy:
#         count = count + 1
#     return count
# print(my_len)

# class Person:
#     mind = "有思想的"
#     animal = "高级动物"
#     faith = "有信仰的"
#     def __init__(self):
#         print(self)
#         print(666)
#     def work(self):
#         print("人类都会工作...")
#     def shop(self):
#         print(self)
#         print("人类都会消费...")
# print(Person())
# print(Person.__dict__)
# print(Person.__dict__["faith"])
# print(Person.__dict__["mind"])
# print(Person.__dict__["work"])
# print(Person.mind)
# print(Person.animal)
# Person.mind = "运用货币"
# print(Person.mind)
# Person.work(1)
# Person.money = "我有钱"
# print(Person.money)
# del Person.mind
# print(Person.__dict__)

# class Person:
#     mind = "有思想的"
#     animal = "高级动物"
#     faith = "有信仰的"
#     def __init__(self,name,age,hobby):
#         self.name = name
#         self.age = age
#         self.hobby = hobby
#     def work(self):
#         print("%s会工作..."% self.name)
#     def shop(self):
#         print("人类可以消费...")
# ret1= Person("alex","23","女人")
# ret2 = Person("太白","23","Alex")
# print(ret1.work())
# ret1.work()
# ret2.work()
# ret2.shop()
