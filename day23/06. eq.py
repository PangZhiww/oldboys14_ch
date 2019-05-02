class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
a = A("alex",23)
aa = A("alex",23)
a2 = A("alex",23)
aa3 = A("alex",23)
a4 = A("alex",23)
a23 = A("alex",23)
aw4 = A("alex",23)
a14 = A("alex",23)
a5 = A("alex",23)
print(a,aa)
print(a == aa == aa3 == a14)    # == 这个语法, 是完全和__eq__相关的