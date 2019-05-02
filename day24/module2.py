import sys
print(__name__)
print(sys.modules["__main__"])  # 获取当前文件的内存地址
print(sys.modules[__name__])