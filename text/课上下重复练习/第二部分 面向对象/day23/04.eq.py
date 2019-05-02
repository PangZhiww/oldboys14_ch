class A:
    def __init__(self,name,age):
        self.name = name
        self.age= age
    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True

a = A("alex",23)
af = A("alex",23)
aa = A("alex",23)
afs = A("alex",23)
fsa = A("alex",23)
ahbfg = A("alex",23)
afd = A("alex",23)
agdf = A("alex",23)
aq = A("alex",23)
gdfa = A("alex",23)
adf = A("alex",23)
# print(a,adf)
print(a == adf == aa == af == afs == agdf)