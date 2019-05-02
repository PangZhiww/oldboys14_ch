# s = '我叫王尼玛'
# print(format(s,'^30'))
# print(format(s,'<30'))
# print(format(s,'>30'))


# 字符串串
# print(format('test', '<20'))    # 左对⻬齐
# print(format('test', '>20'))    # 右对⻬齐
# print(format('test', '^20'))    # 居中

#  数值
# print(format(3, 'b'))   # ⼆二进制
# print(format(97, 'c'))   # 转换成unicode字符
# print(format(11, 'd'))   # ⼗十进制
# print(format(11, 'o'))   # ⼋八进制
# print(format(11, 'x'))   # ⼗十六进制(⼩小写字⺟母)
# print(format(11, 'X'))   # ⼗十六进制(⼤大写字⺟母)
# print(format(11, 'n'))   # 和d⼀一样
# print(format(11))   # 和d⼀一样

#  浮点数
# print(format(123456789, 'e'))   # 科学计数法. 默认保留留6位小数
# print(format(123456789, '0.2e'))   # 科学计数法. 保留留2位小数(小写)
# print(format(123456789, '0.2E'))   # 科学计数法. 保留留2位小数(大写)
# print(format(1.23456789, 'f'))   # 小数点计数法. 保留留6位小数
# print(format(1.23456789, '0.2f'))   # 小数点计数法. 保留留2位小数
# print(format(1.23456789, '0.10f'))   # 小数点计数法. 保留留10位小数
# print(format(1.23456789e+10000, 'F'))   # 小数点计数法. 很大的时候输出 INF(无限大)


# lst = ['蛋1', '蛋2', '蛋3', '蛋4']
# for i in range(len(lst)):
#     print(i)
#     print(lst[i])

# for el in enumerate(lst):   # 把索引和元素(通过元祖)一起获取
#     print(el)

# for index,el in enumerate(lst,1):   # 索引默认从0开始, 可以指定开始的索引
#     print(index)
#     print(el)


# print(all([1,'哈哈','馒头',True]))
# print(any([0,'哈哈','馒头',False]))


# lst1 = ['施瓦辛格','泰达米尔','阿米尔汗','威震天']
# lst2 = ['终结者','英雄联盟','我滴个神','变形金刚']
# lst3 = [1000,2,3,56,87]
# print(zip(lst1,lst2,lst3))
# for el in zip(lst1,lst2,lst3):
#     print(el)