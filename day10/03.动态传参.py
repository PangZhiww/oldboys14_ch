# def chi(*food):     # 可以穿入任意的位置参数
#     print("我要吃",food)   # 动态参数接收到的是tuple类型的数据
#
# chi("盖浇饭","辣条","汉堡")

# 位置参数 > *动态参数 > 默认值参数 > **kwargs
# def chi(a,b,c,*args,d=5):
#     print(a,b,c,d,args)
#
# # chi(1,2,3,4,5,6,7,8)
# chi(1,2,3,4,5,6,7,8,d = "马大哈")

# 写函数, 给函数传递任意个整数, 返回这些数的和

# def he(*n):
#     sum = 0
#     for e in n:
#         sum = sum + e
#     return sum
#
# print(he(5,6,7))


# 动态接受关键字参数
# 1. *位置参数
# 2. **关键字参数
# def func(**food):   # **food动态接胡搜关键字参数
#     print(food)     # 接受到的是字典
#
# func(good_food="盖浇饭",bad_food="辣条",drink="肥宅快乐水",shunx="有无顺序呢",老师="老师的没有顺序")


# 关键字参数一定在位置参数后面
# 这个函数可以接收所有的参数(无敌的)
# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
# func(1, 2, 5, 6, name="taibai",age=18, sex="不详")


# 把列表中的每一个元素作为参数, 传递给函数. 一次都传过去

def func(*args, **kwargs):  # *表示聚合,所有的位置参数, 聚合成元组 **聚合成字典
    print(args)
    print(kwargs)


lst = ["马虎疼", "大洋哥", "小花生", "毛尖妹妹","杜十娘"]
func(*lst)  # 实参, 打散, 迭代产生的
# func(lst[0], lst[1], lst[3])
#
# s = "我不知道写点什么"
# func(*s)

# dic = {"name":"太白", "alex":"wuse"}
# func(**dic) # 把字典打散. 以key=value形式进行传参

# def fun(**kwargs):
#     print(kwargs)
#
# dic = {'a':156, 'b':2.2,'c':6}
# fun(**dic)



# def fun(**kwargs):
#     print(kwargs)
#
# dic = {'a':145, 'b':2}
# fun(**dic)



def func(a, b):
    '''
    计算a+b的和, 返回一个数
    :param a: 第一个数
    :param b: 第二个数
    :return: 返回计算之后的和
    '''
    return a + b