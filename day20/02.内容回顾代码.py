class A:
    def __init__(self,name,age,weight):
        self.name = name
        self.__age = age
        self.__weight = weight

    def func(self):
        print(self.__age)
        print(self.__weight)

a1 = A("顾亚辉", 18 ,45)
print(a1.name)
# print(a1 .__dict__)
a1.func()