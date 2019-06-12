# class Student:
#     def __init__(self,name):
#         self.name = name
#     def check_course(self):
#         print("check_course")
#     def choose_course(self):
#         print("choose_course")
#     def choosed_course(self):
#         print("查看已选择的课程")
# stu = Student(22)
# num = input(">>>")
# if num == "check_course":
#     stu.check_course()
# elif num == "choose_course":
#     stu.choose_course()
# elif num == "choosed_course":
#     stu.choosed_course()


# class Student:
#     ROLE = "STUDENT"
#     @classmethod
#     def check_course(cls):
#         print("查看课程了")
#     @staticmethod
#     def login():
#         print("登录")
# # print(Student.ROLE)
# # print(getattr(Student,"ROLE"))
#
# getattr(Student,"check_course")()
# getattr(Student,"login")()
#
# num = input("你好吗? ")
# if hasattr(Student,num):
#     getattr(Student,num)

# class A():
#     def __init__(self,name):
#         self.name = name
#     def func(self):
#         print("in func")
# a = A("alex")
# print(a.name)
# print(getattr(a,"name"))
# getattr(a,"func")()

# import os
# os.rename("__init__.py","init")
# getattr(os,"rename")("init","__init__.py")
# rename = os.rename
# rename2 = getattr(os,"rename")
# rename2("__init__.py","init")
# rename("init","init2")

# def wahaha():
#     print("wahaha")
# def qqxing():
#     print("qqxing")
# wahaha()
# qqxing()

class Manager:
    OPERATE_DIC = [
        ("创造学生账号","create_student"),
        ("创建课程","create_course"),
        ("查看学生信息","check_student_info"),
    ]
    def __init__(self,name):
        self.name = name
    def create_student(self):
        print("创建学生账号")
    def create_course(self):
        print("创建课程")
    def check_student_info(self):
        print("查看学生信息")
class Student:
    OPERATE_DIC = [
        ("查看所有课程","check_course"),
        ("选择课程","choose_course"),
        ("查看已选择的课程","choosed_course"),

    ]
    def __init__(self,name):
        self.name = name
    def check_course(self):
        print('check_course')
    def choose_course(self):
        print('choose_course')
    def choosed_course(self):
        print('查看已选择的课程')


def login():
    username = input("user: ")
    password = input("ped: ")
    with open("userinfo") as f:
        for line in f:
            user,pwd,ident = line.strip().split("|")
            if user == username and pwd==password:
                print("登陆成功!")
                return username,ident
import sys
def main():
    usr,id = login()
    print("user,id :",usr,id)
    file = sys.modules["__main__"]
    cls = getattr(file,id)
    obj = cls(usr)
    operate_dic = cls.OPERATE_DIC
    while 1:
        for num,i in enumerate(operate_dic,1):
            print(num,i[0])
        choice = int(input("num..."))
        choice_item = operate_dic[choice-1]
        getattr(obj,choice_item[1])()
main()

