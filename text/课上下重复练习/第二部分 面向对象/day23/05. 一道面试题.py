# 一个类
# 对象的属性: 姓名, 性别, 年龄  部门
# 员工管理系统
# 内部转岗 Python开发 ==> go开发
# 姓名, 性别, 年龄  部门

# 1000个员工
# 如果几个员工对象的姓名和性别相同, 这是一个人
# 请对这1000个员工做去重

# class Employee:
#     def __init__(self,name,age,sex,partment):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.partment = partment
#     def __hash__(self):
#         return hash("%s%s" % (self.name,self.sex))
#     def __eq__(self, other):
#         if self.name == other.name and self.sex == other.sex:
#             return True
#
# employ_lst = []
# for i in range(300):
#     a = Employee("alex", i, "male", "python")
#     b = Employee("taibai", i, "女", "python")
#     c = Employee("wusir", i, "男", "python")
#     employ_lst.append(a)
#     employ_lst.append(b)
#     employ_lst.append(c)

# print(employ_lst)
# print(set(employ_lst))
# employ_lst = set(employ_lst)
# for person in employ_lst:
#     print(person.__dict__)


class Employee:
    def __init__(self,name,age,sex,partment):
        self.name = name
        self.age = age
        self.sex = sex
        self.partment = partment
    def __hash__(self):
        return hash("%s%s" % (self.name,self.sex))
    def __eq__(self, other):
        if self.name == other.name and self.sex == other.sex:
            return True
employ_lst = []
for i in range(300):
    employ_lst.append(Employee("alex",i,"mile","python"))
for i in range(300):
    employ_lst.append(Employee("wusir", i, "mile", "python"))
for i in range(300):
    employ_lst.append(Employee("taibai",i,"mile","python"))
# print(employ_lst)
# print(set(employ_lst))
employ_lst = set(employ_lst)
# print(employ_lst)
for person in employ_lst:
    print(person.__dict__)