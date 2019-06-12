class A:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    def func(self):
        print("self.__age")
a1= A("alex",18,46)
# print(a1.name)
# print(a1.__dict__)
# print(a1.age)
a1.func()