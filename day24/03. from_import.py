# from my_module import login
# 不是Python解释器发现的错误, 而是pycharm根据它的一些判断而得出的结论

# from import   的时候发生了什么
# 仍然相当于执行了整个py文件

# 在from import的时候命名空间的变换
# login()
# 导入了什么, 就能使用什么, 不导入的变量, 不能使用
# 不导入并不意味着不存, 而是没有建立文件到模块中其他名字的引用

# def login():
#     print("in my login")
# 当模块中导入的方法或者变量和本文件重名的时候, 那么这个名字只代表最后一次对它复制的那个方法或者变量
# login()
# from my_module import login
# login()
# from my_module import name
# print(name)
# name = "太亮"
# print(name)
# login()
# 在本文件中对全局变量的修改, 是完全不会影响到模块中的变量引用的

# 重命名
# from my_module import login as l
# l()

# 导入多个
# from my_module import login,name
# login()
# print(name)
# name = "太亮"
# login()
# print(name)

# 导入多个之后再重命名
# from my_module import login as l,name as i
# l()
# print(i)

# from 模块 import *
# from my_module import *
# login()
# name

# __all__   可以控制*导入的内容
from my_module import *
login()
name
from  my_module import name
print(name)