# def func():
#     a = 10
#     print(locals())  # 当前作用域中的内容
#     print(globals())  # 全局作用域中的内容
#     print("今天内容很简单")
#
# func()
# print(locals())     # 当前作用域中的内容
# print(globals())        # 全局作用域中的内容


# lst = ['大阳哥','喜欢','私密的散步']
# it = iter(lst)  # __iter__
# # it = lst.__iter__()
# print(it.__next__())
# print(next(it))     # __next__
# print(next(it))


# print('李嘉诚','黄花菜','马云',sep='*',end='大阳哥')


# a = 10
# print(callable(a))

# def func():
#     print('麻花藤')
#
# print(callable(func))     # 函数是可以被调用的


# s = input('请输入a+b:')
# print(eval(s))    # 可以动态的执行代码, 代码必须有返回值

# s = 'for i in range(10): print(i)'
# eval(s)   # False

# s = '25*4'
# print(eval(s))  # 简单运算


# s = '25*4'
# print(exec(s))  # exec 执行代码不返回任何内容


# s = 'for i in range(10): print(i)'
# print(exec(s))

# 动态执行代码
# exec('''
# def func():
#     print('我是周杰伦')
# func()
# ''')
# func()    # 同样可以在函数外侧执行


code1 = "for i in range(10): print(i)"
com = compile(code1, '', mode='exec')   # compile并不会执行你的代码, 只是编译
# print(com)
# exec(com)   # 执行编译之后的结果

# code2 = '5+6+7'
# com2 = compile(code2, '', mode='eval')
# print(eval(com2))

# code3 = "name = input('请输入大阳哥的名字:')"
# com3 = compile(code3, "", mode="single")
# exec(com3)
# print(name)


# print(abs(-2))  # 绝对值
# print(abs(2))

# print(divmod(10,3))     # 求商和余数

# print(round(4.5))   # 五舍六入

# print(pow(10,10))   # a 的 b 次方

# print(pow(10,2,3))  # 如果给了第三个参数, 表示最后取余

# print(sum([1,2,3,4,5,6,7,8,9,10]))  # 求和


# lst = ['猴哥','八戒','师弟']
# it= reversed(lst)   # 不会改变原列表, 返回一个迭代器, 设计上的一个规则
# print(list(it))

# lst = [1,2,3,4,5,6,7]
# print(lst[1:3:1])
#
# s = slice(1,3,1)    # 切片用的
# print(lst[s])


# name = '你好,\n我叫%s周润发' % '马化腾'
# print(name)
# print(repr(name))   # 原样输出, 过滤掉转义字符,不起作用   \n \t \r 不管百分号


# print(ord('a'))   # 97  返回的是字母a在编码表中的码位
# print(ord('中'))   # 20013 '中'字在编码表中的位置
# 一次只能查询一个字符

# print(chr(65))    # 已知码位, 计算字符
# print(chr(20016))



# for i in range(65536):
#     print(chr(i),end=' ')


# print(ascii('个'))


# bs = bytes('大阳哥今天很厉害',encoding='utf-8')
# print(bs)
# print(bs.decode('utf-8'))


# ret = bytearray('alex',encoding='utf-8')    # 仅仅在英文的时候使用bytearray
# print(ret[0])
# ret[0] = 65
# print(str(ret))


# s = memoryview('麻花藤'.encode('utf-8'))   # 查看内存
# print(s)