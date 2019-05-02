# class Person:
#     mind = "有思想的"
#     animal= "高级动物"
#     faith = "有信仰"
#
#     def __init__(self,name,age,sex,hobby):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.hobby = hobby
#
#     def work(self):
#         print("人类都会工作...")
#     def shop(self):
#         print("人类都会消费...")
#     def add_func(self):
#         print("姓名:%s, 年龄:%s, 性别:%s, 爱好:%s" % (self.name,self.age,self.sex,self.hobby))

# 增删改查操作
# print(Person.mind)    # 查询
# print(Person.animal)  # 查询
# Person.money = "运用货币"   # 增加
# Person.mind = "脑残的"   # 改
# del Person.mind
# print(Person.__dict__)


# ret = Person("alex",85,"不男不女","教书")
# ret1 = Person("alex",66,"女","吃屎")
# ret.hight = 175
# # del ret.name
# ret.name = "taibai"
# # print(ret.__dict__)
# # ret.work()
# ret.add_func()
# ret1.add_func()