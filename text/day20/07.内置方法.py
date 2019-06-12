class A:
    def __call__(self, *args, **kwargs):
        print("执行call方法")
    def call(self):
        print("执行call方法了")
class B:
    def __init__(self,cls):
        print("实例化A之前做一些事情")
        self.a = cls()
        self.a()
        print("在实例化A之后做一些事情")
A()()
A.call(11)
B(A)
# print(B.mro())
