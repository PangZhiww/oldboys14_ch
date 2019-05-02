# __ste__: str(obj), 要求必须实现__str__, 要求这个方法的返回值必须是字符串str类型
    # print  $s  str

# __repr__: 是__str__的备胎. 如果有__str__方法, 那么# print  $s  str都先去执行__str__方法, 并且使用__str__的返回值.
    # 如果没有__str__, 那么# print  $s  str都会执行repr
    # repr(obj), %r

# 在子类中中使用__ste__ 先找子类的__ste__ 没有的话要想上找, 只要父类不是object. 就执行父类的__str__ .
# 但是如果除了object之外的父类都没有__str__方法, 就执行子类的__repr__方法, 如果子类也没有
# 还要向上继续找父类中的__repr__方法.
# 一直找不到, 再执行object类中的__str__方法

# a = 123
# print(a)
# print(repr(a))

# class A:
#     def __init__(self,name):
#         self.name = name
#     # def __str__(self):
#     #     return "**%s**" % self.name
#     def __repr__(self):
#         return self.name
#
# a = A("alex")
# print(a)
# print(str(a),repr(a))
# print("%s | %r" % (a,a))


# print("--%s--" % ("alex"))
# print("--%r--" % ("alex")).



# 如果 __str__   和    __repr__?
#     优先使用 __repr__



class A:
    def __init__(self,name):
        self.name = name
    # def __str__(self):
    #     return "**%s**" % self.name
    def __repr__(self):
        return self.name

class B(A):
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return self.name

a = B("alex")
print(a)
print(str(a),repr(a))
print("%s | %r" % (a,a))