# 什么是反射
#   用字符串数据类型的变量名来访问(查看)这个变量的值
# 反射的方法:
#     1. getattr() >好朋友一般一起用<  2. hasattr()/   3. setattr()   4. delattr()


# class Student:
#     ROLE = "STUDENT"  # 静态属性
#     def __init__(self,name):
#         self.name = name  # 属性
#     def check_course(self):
#         print("check_course")   # 动态属性
#     def choose_course(self):
#         print("choose_course")
#     def choosed_couse(self):
#         print("查看已选择的课程")

# 备用
# class Student:
#     ROLE = "STUDENT"    # 静态属性
#     def __init__(self,name):
#         self.name = name    # 属性
#     @classmethod    #　反射调用类方法
#     def check_course(cls):
#         print("查看课程了!!!")
#
#     @staticmethod   # 反射调用静态方法
#     def login():
#         print("登陆!")


#
# stu = Student()
# num = input(">>>")
# if num == "check_course":
#     stu.check_course()
# elif num == "chosse_course":
#     stu.choose_course()
# elif num == "choosed_course":
#     stu.choosed_couse()


# eval 这个东西慎用 明确的写在你的代码里

# 类
# 命名空间.XXX == getattr(命名空间, "XXX")      取到是方法加()    是属性直接用
#   能用类调用的: 静态属性(字段)(属性)    类方法    静态方法
# getattr(A,B) # 第一个参数的命名空间中的变量名为第二个参数的变量的值
#         ^ ^
# A命名空间  B变量的值

# 静态属性(变量)
# class Student:
#     ROLE = "STUDENT"  # 静态属性
#
# # print(Student.ROLE)
# "ROLE"
# print(getattr(Student,"ROLE"))


# 反射调用类方法
# class Student:
#     ROLR = "STUDENT"  # 静态属性
#     @classmethod    # 类方法
#     def check_course(self):
#         print("查看课程了!!!")     # 动态属性
# # 反射查看属性
# print(Student.ROLR)
# print(getattr(Student,'ROLR'))

# 反射调用(类)方法
# print(getattr(Student,"check_course"))    # 打印出来内存地址
# getattr(Student,"check_course")()     # 调用类方法



# 反射调用静态方法
# class Student:
#     ROLE = "STUDENT"  # 静态属性
#     @classmethod
#     def check_course(cls):
#         print("查看课程了!!!")
#
#     @staticmethod   # 反射调用静态方法
#     def login():
#         print("登陆!")
# #
# # # print(getattr(Student,"login"))
# # getattr(Student,"login")()  # 调用静态方法
#
# num = input(">>>")
# # print(hasattr(Student,num))     # hasattr 表示输入的字符串(num)是否在命名空间(Student)中找得到
# if hasattr(Student,num):     # hasattr 表示输入的字符串(num)是否在命名空间(Student)中找得到
#     getattr(Student,num)()






# 对象
    # 方法   对象属性
# class A:
#     def __init__(self,name):
#         self.name = name    # 属性
#     def func(self):
#         print("in func")    # 动态属性
#
# a = A("alex")   # 实例化对象
# print(a.name)
# print(getattr(a,"name"))   # 取属性
# getattr(a,"func")()     # 取动态属性





# 模块
# import os   # 别人写好的Python代码的结合
# # os.rename("__init__.py","init")
# # print(getattr(os,"rename"))
# # getattr(os,"rename")    # == os.rename
# # getattr(os,"rename")("init","__init__.py")
#
# # print(os.rename)
# # os.rename()
# # print("aaa")    # 内置函数   一共68个
# # print(getattr(os,'rename'))
# # rename = os.rename
# # rename2 = getattr(os,"rename")
# # rename("__init__.py","init")    # os.rename("__init__.py","init")
# # rename2("init","__init__.py")    # os.rename("init","__init__.py")
#
#
# os.rename("init","__init__.py")
# os.rename("__init__.py","init")


# func = os.rename
# func()











# def wahaha():
#     print("wahaha")
#
# def qqxing():
#     print("qqxing")

# 反射自己模块中的内容
    # 找到自己当前文件所在的命名空间
# wahaha()
# qqxing()

# import sys
# print(sys.modules)
# import 相当于导入了一个模块
# 模块哪个导入了, 哪个没导入    在我的Python解释器里应该记录下来
# import sys 是一个模块, 这个模块里的所有的方法都是和Python解释器相关的
# sys.modules 这个方法, 表示所有在当前这个Python程序中导入的模块

# <module '__main__' from 'D:/practice/Python/oldboys14/day21/04.反射.py'>
# print(sys.modules["__main__"])
# my_file = sys.modules["__main__"]
# my_file.wahaha()
# my_file.qqxing()
# getattr(my_file,"wahaha")()
# getattr(my_file,"qqxing")()






# 复习
# hasattr();getattr()
# 类名,名字
    # getattr(类名,"名字")
# 对象名,名字
    # getattr(对象,"名字)
# 模块名,名字
    # import 模块
    # getattr(模块,"名字")
# 自己文件,名字
#     import sys
    # getattr(sys.modules["__main__"],"名字")




# 选课系统代码
# login
# 判断身份, 并且根据身份实例化
# 根据每个身份对应的类, 让用户选择能够做的事情


# class Manager:
#     OPERATE_DIC = [
#         ("创建学生","create_student"),
#         ("创建课程","create_course"),
#         ("查看学生信息","create_student_info")
#     ]
#     def __init__(self,name):
#         self.name = name
#     def create_student(self):
#         print("创建学生账号")
#     def create_course(self):
#         print("创建课程")
#     def create_student_info(self):
#         print("查看学生信息")
#
#
# class Student:
#     OPERATE_DIC = [
#         ("查看所有课程", "check_course"),
#         ("选择课程", "choose_course"),
#         ("查看已选择课程", "choosed_couse")
#     ]
#     def __init__(self,name):
#         self.name = name
#     def check_course(self):
#         print("check_course")
#     def choose_course(self):
#         print("choose_course")
#     def choosed_couse(self):
#         print("查看已选择的课程")
#
# def login():
#     username = input("user: ")
#     password = input("pwd: ")
#     with open("userinfo") as f:
#         for line in f:
#             user,pwd,ident = line.strip().split("|")    # ident = 'Manger\n'
#             if user == username and pwd == password:
#                 print("登陆成功!")
#                 return username,ident
#             else:
#                 print("登陆失败! 账号密码错误!")
#
# import sys
# def main():
#     usr,id = login()
#     print("user,id: ",usr,id)
#     # if id == "Manger":     # 笨办法
#     #     Manger(usr)
#     # elif id == "Student":
#     #     Student(usr)
#     file = sys.modules['__main__']
#     cls = getattr(file,id)    # Manager = getattr(当前文件, "Manager")
#
#     # print(Student,Manager)
#     # print(cls)
#
#     obj = cls(usr)
#     operate_dic = cls.OPERATE_DIC
#     # print(operate_dic)
#     while True:
#         for num,i in enumerate(operate_dic,1):
#             print(num,i[0])
#         choice = int(input("请输入序号num: "))
#         choice_item = operate_dic[choice - 1]
#         getattr(obj,choice_item[1])()
#
# main()


#
# l = ["a","b","c"]
# for num,i in enumerate(l,1):
#     print(num,i)


# class Manager:
#     OPERATE_DIC = [
#         ("创建学生","create_student"),
#         ("创建课程","create_course"),
#         ("查看学生信息","create_student_info")
#     ]
#     def __init__(self,name):
#         self.name = name
#     def create_student(self):
#         print("创建学生账号")
#     def create_course(self):
#         print("创建课程")
#     def create_student_info(self):
#         print("查看学生信息")
# class Student:
#     OPERATE_DIC = [
#         ("查看所有课程", "check_course"),
#         ("选择课程", "choose_course"),
#         ("查看已选择课程", "choosed_couse")
#     ]
#     def __init__(self,name):
#         self.name = name
#     def check_course(self):
#         print("查看所有课程")
#     def choose_course(self):
#         print("选择课程")
#     def choosed_couse(self):
#         print("查看已选择的课程")
# def login():
#     username = input("user: ")
#     password = input("pwd: ")
#     with open("userinfo") as f:
#         for line in f:
#             user, pwd, ident = line.strip().split("|")    # ident = 'Manger\n'
#             if user == username and pwd == password:
#                 print("登陆成功!")
#                 return username,ident
#             else:
#                 print("登陆失败! 账号密码错误!")
# import sys
# def main():
#     usr,id = login()
#     print("user,id: ", usr, id)
#     file = sys.modules['__main__']
#     cls = getattr(file,id)    # Manager = getattr(当前文件, "Manager")
#     obj = cls(usr)
#     operate_dic = cls.OPERATE_DIC
#     while True:
#         for num,i in enumerate(operate_dic,1):
#             print(num,i[0])
#         choice = int(input("请输入序号num: "))
#         choice_item = operate_dic[choice - 1]
#         getattr(obj,choice_item[1])()
# main()





# setattr
# class A:
#     def __init__(self,name):
#         self.name = name
#
# a = A("alex")
# # a.name = "alex_SB"
# # getattr(a,"name")
# setattr(a,"name","alex_SB")
# print(a.name)


class A:
    def __init__(self,name):
        self.name = name

a = A("alex")

# print(a.__dict__)
# del a.name

print(a.__dict__)
delattr(a,"name")
print(a.__dict__)