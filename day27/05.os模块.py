import os
# 与工作目录相关
# os.chdir("D:\practice\Python\oldboys14\day27")
# print(os.getcwd())  # 在哪个地方执行这个文件, getcwd的结果就是哪个路径
# print(__file__)
#
# print(os.curdir)
# print(os.pardir)


# 创建文件/文件夹  删除文件/文件夹
# import os
# os.mkdir("dir")   # ftp 网盘  创建文件夹     创建单级目录
# os.mkdir("dir/dir5")   # ftp 网盘  创建文件夹     创建单级目录
# os.makedirs("dir2/dir3/dir4",exist_ok=True)    # 创建多级目录

# os.rmdir("dir/dir5")  # 删除单个文件
# os.rmdir("dir2/dir3/dir4")  # 不能删除一个非空文件夹
# os.removedirs("dir2/dir3/dir4")     # 删除多级目录
# 递归向上删除文件夹, 只要删除当前目录之后, 发现上一级目录也为空了,就把上一级目录也删掉
    # 如果发现上一级目录有其他文件, 就停止


# print(os.listdir("D:\practice\Python\oldboys14"))   # 列出目录下的所有文件和子目录, 包括隐藏文件, 并以列表方式打印

# print(os.stat(r'D:\practice\Python\oldboys14'))   # stat 结构
# print(os.sep)  # 当前你所在的操作系统的目录分割符 \   /a/dir/dir2
# print([os.linesep])  #输出当前平台使用的行终止符，win下为"\r\n",Linux下为"\n"
# print(os.pathsep) #   输出用于分割文件路径的字符串 win下为;,Linux下为:
# print(os.name) # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'


# 学生选课系统
# base_path = 'D:\sylar\python_workspace'
# s = 'day25'
# os.sep.join(base_path,s)
# if os.name == 'nt':
#     '\\'.join(base_path,s)
# else:
#     '/'.join(base_path, s)

# os.system('dir')  # 删除文件 copy文件
# ret = os.popen('dir')  # 查看当前路径 查看某些信息
# print(ret.read())
# print(type(ret.read()))

# print(os.environ)


# print(os.path.abspath("4.sys模块.py"))
# print([os.path.abspath("4.sys模块.py")])
# print([os.path.abspath(r"D:\practice\Python\oldboys14\day27\03.时间模块.py")])
# print(os.path.split(r"D:\practice\Python\oldboys14\day27\03.时间模块.py"))
# print(os.path.split(r"D:\practice\Python\oldboys14\day27"))
# print(os.path.dirname(r"D:\practice\Python\oldboys14\day27\03.时间模块.py"))
# print(os.path.basename(r"D:\practice\Python\oldboys14\day27\03.时间模块.py"))
# print(os.path.exists(r"D:\practice\Python\oldboys14\day27\05.os模块.py"))
# print(os.path.isfile(r"D:\practice\Python\oldboys14\day27\05.os模块.py"))
# print(os.path.isfile(r"D:\practice\Python\oldboys14\day27"))
# print(os.path.isdir(r"D:\practice\Python\oldboys14\day27\05.os模块.py"))
# print(os.path.isdir(r"D:\practice\Python\oldboys14\day27"))
# ret = os.path.join(r"D:\practice\Python\oldboys14\day27\__init__.py")
# print(os.path.abspath(ret))

# print(os.path.getsize(r"D:\practice\Python\oldboys14\day27\__init__.py"))
# print(os.path.getsize(r"D:\practice\Python\oldboys14\day27\04.sys模块.py"))
# print(os.path.getsize(r"D:\practice\Python\oldboys14\day27"))