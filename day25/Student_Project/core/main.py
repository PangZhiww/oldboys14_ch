from core import auth
from core import stuudent
from core import manager

def entry_point():
    print("欢迎进入学生选课系统: ")
    auth.login()
    print(stuudent.Studeny)
    print(manager.Manager)

if __name__ == "__main__":
    entry_point()