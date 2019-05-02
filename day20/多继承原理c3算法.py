class H:
    def bar(self):
        print("F.bar")


class G(H):
    def bar(self):
        print("F.bar")


class F(H):
    def bar(self):
        print("F.bar")


class E(G):
    def bar(self):
        print("E.bar")


class D(F):
    def bar(self):
        print("D.bar")


class C(E):
    def bar(self):
        print("C.bar")


class B(D):
    def bar(self):
        print("B.bar")


class A(B, C, D):
    def bar(self):
        print("A.bar")


a = A()
print(A.mro())

# 每个列表的第一个元素为头部, 从第一个列表的头部开始找, 找其他列表中的尾部是否含有这个类名, 如果没有, 提取出来放到一个列表中.    如果有, 继续找下一个列表的头部, 循环下去.
# 只要提取出来一个, 我们就从第一个列表的头部接着重复上面的操作


# A[B,C,D]

# 首先找到A集成的三个类的深度继承顺序, 放到一个列表中
# L[B] = [B,D,F,H]    # B往上面的继承顺序
# L[C] = [C,E,G,H]    # C往上面的继承顺序
# L[D] = [D,F,H]    # D往上面的继承顺序

# 第二步: A自己的广度, 第一层
# L[A] = [B,C,D]

# 提取出来的列表:　list - [A,B,C,D,F,E,G,H,O]

# 1. [B,D,F,H]    [C,E,G,H]   [D,F,H]   [B,C,D]
# 2. [D,F,H]    [C,E,G,H]   [D,F,H]   [C,D]     # 提取了头部的B, 然后将其他列表的头部的B删除, 并将B放到list中
# 3. [D,F,H]    [E,G,H]   [D,F,H]   [D]     # 因为第一个列表的D在其他列表的尾部存在, 所以跳过D, 然后找第二个列表的头部C, 提取头部的C, 然后将其他列表头部的C删除, 并将C放到list中
# 4. [F,H]    [E,G,H]   [F,H]
# 5. [H]    [E,G,H]   [H]
# 6. [H]    [G,H]   [H]
# 7. [H]    [H]   [H]
