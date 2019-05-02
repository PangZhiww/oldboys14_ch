# isinstance()  # 函数来判断一个对象是否是一个已知的类型，类似 type()。    判断对象所属类型, 包括继承
# issubclass()  # 判断类与类之间的继承关系

# class A:pass
# class B(A):pass
# b = B()
# print(isinstance(b,B))   # object, type
# print(isinstance(b,A))   # object, type
# l = list()
# print(l)    # type(l)
# print(type(l))
# class mystr(str):pass
# ms = mystr("str")
# print(ms)
# print(type(ms) is str)  # 不包含继承关系, 只管一层
# print(isinstance("alex",str))   # 包含所有的继承关系


# type("alex") is str
# isinstance("alex") is str

# == 值相等        值运算
# is 内存地址相等      身份运算

# is 要求更苛刻
    # 不仅要求值相等, 还要求内存地址相同


# issubclass()  # 判断类与类之间的继承关系
# class A:pass
# class B:pass
# print(issubclass(B,A))
# print(issubclass(A,B))