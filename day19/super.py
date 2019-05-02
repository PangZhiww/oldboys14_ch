# class A:
#     def f1(self):
#         print('in A f1')
#
#     def f2(self):
#         print('in A f2')
#
#
# class Foo(A):
#     def f1(self):
#         super().f2()
#         print('in A Foo')
#
#
# obj = Foo()
# obj.f1()
#
# super可以下一个类的其他方法



# class A:
#     def f1(self):
#         print('in A')
#
# class Foo(A):
#     def f1(self):
#         super().f1()
#         print('in Foo')
#
# class Bar(A):
#     def f1(self):
#         print('in Bar')
#
# class Info(Foo,Bar):
#     def f1(self):
#         super().f1()
#         print('in Info f1')
#
# obj = Info()
# obj.f1()
#
# '''
# in Bar
# in Foo
# in Info f1
# '''
# print(Info.mro())  # [<class '__main__.Info'>, <class '__main__.Foo'>, <class '__main__.Bar'>, <class '__main__.A'>, <class 'object'>]
#
# super()严格按照类的mro顺序执行




# class A:
#     def f1(self):
#         print('in A')
#
# class Foo(A):
#     def f1(self):
#         super().f1()
#         print('in Foo')
#
# class Bar(A):
#     def f1(self):
#         print('in Bar')
#
# class Info(Foo,Bar):
#     def f1(self):
#         super(Foo,self).f1()
#         print('in Info f1')
#
# obj = Info()
# obj.f1()
#
# 再来!