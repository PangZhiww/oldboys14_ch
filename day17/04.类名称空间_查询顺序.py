# class Person:
#     animal = '高级动物'
#     soul = "有灵魂的"
#     language = "语言"
#
#     def __init__(self,country,name,sex,age,hight):
#         self.country = country
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.hight = hight
#
#     def eat(self):
#         print("%s吃饭" % self.name)
#
#     def sleep(self):
#         print("睡觉")
#
#     def work(self):
#         print("工作")
#
# p1 = Person("菲律宾",'alex','未知',42,175)
# p2 = Person("美国",'武大','男',35,160)
# p3 = Person("中国","太白","女",15,187)
# p4 = Person(p1.country,p2.name,p3.sex,p1.age,p2.hight)
#
# p1.wight = 150
# p1.eat()
# print(p1.__dict__)




# 查询顺序:
#     对象.属性: 先从对象空间找, 如果找不到, 再从类空间找, 再找不到, 再从父类找....
#     类名.属性: 先从对象空间找, 如果找不到, 再从父类找....

# 对象与对象之间是互相独立的,



# 练习题: 计算一个类, 实例化多少对象
# class Count:
#     count = 0
#     def __init__(self):
#         # Count.count = Count.count + 1
#         Count.count = self.count + 1
#
# obj1 = Count()
# obj1 = Count()
# obj1 = Count()
# obj1 = Count()
# obj1 = Count()
# obj1 = Count()
# obj1 = Count()
# print(Count.count)


# count = 0
# def func():
#     print(count)
#
# func()







# class Count:
#     count = 0
#     def __init__(self):
#         pass

# 通过类名可以更改我的类中的静态变量值
# Count.count = 6
# print(Count.__dict__)

# 但是通过对象不能改变只能引用类中的静态变量

# obj1 = Count()
# print(obj1.count)
# print(Count.count)

# obj1.count = 6  # 仅仅可以添加对象中的值