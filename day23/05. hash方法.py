# hash方法
# 底层数据结构基于hash值寻址的优化操作
# hash是一个算法
# 能够把某个要存在内存里的值通过一系列计算
# 保证不同的值的hash结果是不一样的
# "123456789" ==> 924566325
#对同一个值在多次执行python代码的时候, hash值是不同的
# 但是对同一个值, 在同一次执行Python代码的时候hash值永远不变

# 字典寻址  - hash算法()
# d = {"key":"value"}
# hash - 内置函数

# set集合
# se = {1,2,2,3,4,5,"a","b","d","f"}
# print(se)

# d = {"key":"v1","key":"v2"}
# print(d["key"])   # 输出第二个key

# hash(obj) obj内部必须实现了__hash__方法