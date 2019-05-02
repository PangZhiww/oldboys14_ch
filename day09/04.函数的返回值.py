# def yue():
#     print("好几天各地")
#     print("安徽人我提前")
#     print("法国和色黑眼圈")
#
#     return  "大吗"    # return 返回值    当函数结束的时候,给调用方一个结果
#
# ret = yue()
# print(ret)


# 只要函数执行到return 函数就会停止执行
# 1. 每个函数如果在函数中不写return, 默认返回None
# 2. 我们也可以只写一个return, 也是返回None, 停止函数的执行
# 3. return 一个返回值, 你在调用方能接收到一个返回值
# 4. return 多个返回值, 多个值需要用 , 隔开      接收的位置, 接收的是元祖

# def yue():
#     print("很简单有特色人")
#     return      #  函数停止了, 后面就不执行
#     # print("干海参发热丝")
#
# ret = yue()
# print(ret)




def yue():
    print("好几天各地")
    print("安徽人我提前")
    print("法国和色黑眼圈")

    return  "大吗","萝莉","模特"    # 多个返回值在接收的位置接收到的是tuple类型的数据

# ret = yue()
a,b,c = yue()
# print(ret)
print(a)
print(b)
print(c)