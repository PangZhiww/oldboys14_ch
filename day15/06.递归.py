# import sys
# sys.setrecursionlimit(10000)    # 可以调整递归深度, 但是不一定能跑到这里
# def func(count):
#     print("我是谁,我在哪里" + str(count))
#     func(count + 1)
#
# func(1)



# 遍历树形结构
# import os
# filePath = 'E:\software\python\practice\oldboys14'

# def read(filePath,n):
#     it = os.listdir(filePath)   # 查看文件夹中的文件
    # print('__iter__' in dir(it))    # 可迭代对象
    # print('__next__' in dir(it))    # 不是迭代器

    # for el in it:
        # print(el)
        # if os.path.isdir(os.path.join(filePath,el)):   # 判断是文件夹还是文件
        #     print('\t'*n, el)  # 打印文件夹
            # 再次调用本函数
            # read(os.path.join(filePath,el),n+1)
        # else:   # 普通文件, 不是文件夹了
        #     print('\t'*n, el)   # 递归的出口

# read(filePath,0)



import os
filePath = 'E:\software\python\practice\oldboys14'

def func(filePath,n):
    it = os.listdir(filePath)   # 打开文件夹
    for el in it:
        # 拿到路径
        fp = os.path.join(filePath, el) # 获取到绝对路径
        if os.path.isdir(fp):   # 判断是否是文件夹
            print('\t'*n, el)
            func(fp,n+1)    # 又是文件夹, 继续读取内部内容   递归入口
        else:
            print('\t'*n, el)   # 递归出口

func(filePath,0)