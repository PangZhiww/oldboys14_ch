import pickle
# dump的结果是bytes，dump用的f文件句柄需要以wb的形式打开，load所用的f是rb模式
# 支持几乎所有的对象序列化
# 对于对象的序列化需要这个对象对应的类在内存中
# 对于多次dump/load的操作做了良好的处理

# dic = {1:(12,3,4),("a","b"):4}
# pic_dic = pickle.dumps(dic)
# print(pic_dic)
# new_dic = pickle.loads(pic_dic)
# print(new_dic)

# pickle支持几乎所有对象的
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# a1 = Student("alex","83")
# ret = pickle.dumps(a1)
# w1 = pickle.loads(ret)
# print(w1.name)
# print(w1.age)

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# a1 = Student("alex",83)
# with open("pickle_demo","wb")as f:
#     pickle.dump(a1,f)
# with open("pickle_demo","rb")as f:
#     w1 = pickle.load(f)
#     print(w1.name)
#     print(w1.age)

# 学员选课系统 pickle模块来储存每个学员的对象
with open("pickle_demo","wb")as f:
    pickle.dump({"k1":"v1"},f)
    pickle.dump({"k12":"v12"},f)
    pickle.dump({"k2":"v2"},f)
    pickle.dump((9,0.6,3),f)
    pickle.dump({"k4":[1,2,3]},f)
    # pickle.dump({[4,5,6]:"v5"},f)
    pickle.dump({(7,8,9):"v6"},f)
    pickle.dump({"k7":(7,4,1.23)},f)

with open("pickle_demo","rb")as f:
    while True:
        try:
            print(pickle.load(f))
        except EOFError:
            break