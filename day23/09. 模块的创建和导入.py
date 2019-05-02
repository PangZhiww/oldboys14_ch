# import my_module    # 要导入一个py文件的名字, 但是不加 .py 后缀名
# import my_module    # 模块的名字必须要满足变量的命名规范
#                         # 一般情况下, 模块都是小写字母开头的名字


# import这个语句相当于什么?
# import这个模块相当于执行了这个模块所在的py文件

# 模块可以被多次导入吗?   一个模块不会被重复导入

# 如何使用模块呢?
# def login():
#     name = "太亮"
#     print("in mine login")
# login()
# my_module.login()
# print(my_module.name)

# 在导入一个模块的过程中到底发生了哪些事情

# 模块的重命名
# import my_module as m
# m.login()
# my_module.login() # 更改内存当中引用的变量名   改名之后, 找不到文件  报错

# 导入多个模块
# import os
# import os,my_module
# import my_module

# os.rename()
# my_module.login()

# PEP8规范
    # 要求不可以在同一行导入多个模块
# 所有的模块导入都应该尽量放在文件的开头
# 模块的导入是有顺序的
    # 先导入内置模块
    # 再导入第三方模块
    # 最后导入自定义模块