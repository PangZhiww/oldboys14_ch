import sys
# sys.path  # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
# sys.modules   #
# print(sys.platform)   # 返回操作系统平台名称
# sys.exit()  # 结束程序
# print(123)

print(sys.argv) # 命令行参数List，第一个元素是程序本身路径
# 列表
# 第一个元素, 时执行这个文件的时候, 写在Python命令后面的第一个值
# 之后的元素, 在执行Python的启动的时候, 可以写多个值, 都会一次添加到列表中

# 有什么用? 怎么用?
name = sys.argv[1]
pwd = sys.argv[2]
if name == "alex" and pwd == "alex123":
    print("执行以下代码")
else:
    exit()