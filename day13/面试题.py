def add(a,b):
    return a + b

def test():
    for r_i in range(4):
        yield r_i

g = test()

for n in [2,10,5]:
    g = (add(n,i) for i in g)   # 惰性机制
print(list(g))  # 这里所有的n都是10, 都是最后一个值