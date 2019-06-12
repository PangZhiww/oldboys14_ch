# class Manager:
#     OPERATE_DIC = [
#         ('创造学生账号', 'create_student'),
#         ('创建课程', 'create_course'),
#         ('查看学生信息', 'check_student_info'),
#     ]
#
#     def __init__(self, name):
#         self.name = name
#
#     def create_student(self):
#         print('创建学生账号')
#
#     def create_course(self):
#         print('创建课程')
#
#     def check_student_info(self):
#         print('查看学生信息')
#
#
# class Student:
#     OPERATE_DIC = [
#         ('查看所有课程', 'check_course'),
#         ('选择课程', 'choose_course'),
#         ('查看已选择的课程', 'choosed_course')
#     ]
#
#     def __init__(self, name):
#         self.name = name
#     def check_course(self):
#         print('check_course')
#     def choose_course(self):
#         print('choose_course')
#     def choosed_course(self):
#         print('查看已选择的课程')
#
# def login():
#     username = input('user : ')
#     password = input('pwd : ')
#     with open('userinfo') as f:
#         for line in f:
#             user, pwd, ident = line.strip().split('|')  # ident = 'Manager'
#             if user == username and pwd == password:
#                 print('登录成功')
#                 return username, ident
#
# import sys

# def main():
#     usr, id = login()
#     print('user,id :', usr, id)
#     file = sys.modules['__main__']
#     cls = getattr(file, id)  # Manager = getattr(当前文件,'Manager')
#     obj = cls(usr)
#     operate_dic = cls.OPERATE_DIC
#     while True:
#         for num, i in enumerate(operate_dic, 1):
#             print(num, i[0])
#         choice = int(input('num >>>'))
#         choice_item = operate_dic[choice - 1]
#         getattr(obj, choice_item[1])()
#
# main()


import sys
class Manager:
    OPERATE_DIC = [
        ("创建学生","create_student"),
        ("创建课程","create_course"),
        ("查看学生信息","create_student_info")
    ]
    def __init__(self,name):
        self.name = name
    def creata_student(self):
        print("创建学生账号")
    def create_course(self):
        print("创建课程")
    def create_student_info(self):
        print("查看学生信息")
class Student:
    OPERATE_DIC = [
        ("查看所有课程","check_course"),
        ("选择课程","choose_course"),
        ("查看已选择的课程","choosed_couse")
    ]
    def __init__(self,name):
        self.name = name
    def check_course(self):
        print("查看所有课程")
    def choose_course(self):
        print("选择课程")
    def chooosed_couse(self):
        print("查看已选择的课程")
def login():
    usernamne = input("username: ")
    password = input("password: ")
    with open("userinfo") as f:
        for line in f:
            user,pwd,ident = line.strip().split("|")
            if user == usernamne and pwd == password:
                print("登陆成功!")
                return usernamne,ident
            else:
                print("登陆失败!")

def main():
    usr,id = login()
    print("user,id:",usr,id)
    file = sys.modules["__main__"]
    cls = getattr(file,id)
    obj = cls(usr)
    operate_dic = cls.OPERATE_DIC
    while 1:
        for num,i in enumerate(operate_dic,1):
            print(num,i[0])
        choice = int(input("请输入序号:"))
        choice_item = operate_dic[choice - 1]
        getattr(obj,choice_item[1])()
main()