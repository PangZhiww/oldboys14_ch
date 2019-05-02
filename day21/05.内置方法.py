# __名字__
    # 类中的特殊方法(中文书)
    # 双下方法  *
    # 魔术方法  *
    # 内置方法(中文书)

# 类中的每一个双下方法都有它自己的特殊意义


# __call__  flask django

# class A:
#     def __call__(self, *args, **kwargs):
#         print("执行__call__方法")
# a = A()()
# a()   # 对象()  相当于调用__call__方法
# A()()     # 类名()(), 相当于线实例化得到一个对象, 再对对象(), ==> 和上面的结果一样, 相当于调用__call__方法



# class A:
#     def __call__(self, *args, **kwargs):
#         print("执行__call__方法")
#     def call(self):
#         print("执行call方法了")
# class B:
#     def __init__(self,cls):
#         print("实例化A之前做一些事情")
#         self.a = cls()
#         self.a()
#         print("实例化A之后做一些事情")

# A()()   # 和上面的结果一样, 相当于调用__call__方法
# B(A)










# __len__
# 内置函数和类的内置方法是有奸情的

# len(dict)   tuple   str   list   set
# def iter(obj):
#     return obj.__iter__()

# l = [1,2,3]
# l.__iter__()
# iter(l)   # l.__iter__()

# class mylist:
#     def __init__(self):
#         self.lst = [1,2,3,4,5]
#         self.name = "alex"
#         self.age = 83
#     def __len__(self):
#         print("执行len函数了")
#         # return 3
#         # return len(self.lst)    # lst长度
#         return len(self.__dict__)    # 多少属性
#
# l = mylist()
# len(l)
# print(len(l))   # len(obj)相当于调用了这个对象的__len__方法
# len(obj)相当于调用了这个obj的__len__方法
# __len__方法return的值就是len函数的返回值
# 如果一个obj对象没有__len__方法,那么len函数会报错

# 对象没有长度
# print(l)
# print(l.lst)

# 练习
# 类
# self.s = ""
# len(obj) = str 的长度

# class Lei:
#     def __init__(self):
#         self.name = "alex"
#         self.age = 28
#         self.lst = [2,3,4,5,6,7,8,9,0]
#
#     def __len__(self):
#         print("执行__len__方法")
#         # return len(self.lst)
#         # return len(self.__dict__)
#         return len(self.name)
#
# l = Lei()
# print(len(l))

# 老师讲的
# class My:
#     def __init__(self,s):
#         self.s = s
#     def __len__(self):
#         return len(self.s)
#
# my = My("abgdfgsc")
# print(len(my))







# iter和next的列子
# __iter__
# __next__
# def iter(obj):
#     return obj,__iter__()
# l = [1,2,3]
# iter(l)    # l.__iter__()






# __new__   ==> # 构造方法  (创造)    开辟内存空间的类的构造方法
# 特别重要(单例类)

# 构造方法
# __init__ # ==> 初始化方法
# class Single:
#     def __new__(cls, *args, **kwargs):
#         # print("在new方法里")
#         obj = object.__new__(cls)
#         print("在new方法里", obj)
#         # return object.__new__(cls)
#         return obj
#
#     def __init__(self):
#         print("在init方法里",self)

# obj = Single()
# single的new, single没有, 只能调用object的new方法
# new方法在什么时候执行?
#     在实例化之后, 在__init__之前先执行new来创建一块空间


# 单例
    # 如果一个类, 从头到尾只有一个实例, 说明从头到尾只开辟了一块属于对象的空间, 那么这个类就是一个单例类
# class A:
#     pass
# a = A()
# a2 = A()
# a3 = A()
# print(a,a2,a3)

# 写一个单例类
# class Single:
#     __ISINCTANCE = None
#     def __new__(cls, *args, **kwargs):
#         if not cls.__ISINCTANCE:
#             cls.__ISINCTANCE = object.__new__(cls)
#         return cls.__ISINCTANCE
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# s1 = Single("alex",83)
# s2 = Single("taibai",40)
# print(s1.name)
# print(s2.name)
# print(s1,s2)





# 面向对象在实例化的时候需要做的三件事情:
    # 1. 开辟一个空间, 属于对象的
    # 2. 吧对象的空间创给self, 执行init
    # 3. 将这个对象的空间返回给调用者








# __str__ / __repr__
# l = [1,2,3]     # 实例化一个list的对象
# # l 是个对象
# print(l)

class Student:
    def __str__(self):
        return '%s %s %s' % (self.school,self.cls,self.name)
    def __init__(self,name,stu_cls):
        self.name = name
        self.school = "old boy"
        self.cls = stu_cls
he = Student("hezewei","py14")
# print(he)
# print(he.name)
huang = Student("huangdongyang",'py15')
# print(huang)
# print(huang.name)
print(str(he))    # 内置的数据类型, 内置的类    相当于执行__str__
print("学生1 : %s" % he)

# print一个对象相当于调用一个对象的__str__方法      直接打印对象的时候     ==>       都是返回值
# str(obj)   相当于执行obj.__str__方法         强转数据类型的时候     ==>       都是返回值
# '%s' %obj 相当于执行obj.__str__方法          格式化的时候      ==>       都是返回值





# 总结
    # 所有的双下方法, 没有需要你在外部直接调用的
    # 而是总有一些其他的 内置函数 特殊语法, 来自动出发这些 双下方法