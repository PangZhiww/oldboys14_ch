import hashlib
# 能够把一个字符串数据类型的变量
# 转换成一个 定长的 密文的 字符串，字符串里的每一个字符都是一个十六进制数字

# 对于同一个字符串，不管这个字符串有多长，只要是相同的
# 无论在任何环境下，多少次执行，在任何语言中
# 使用相同的算法\相同的手段得到的结果永远是相同的
# 只要不是相同的字符串，得到的结果一定不同

# 登陆的密文验证

# 字符串 --> 密文
# 密文 不可逆 字符串

# 算法: 对于同一个字符串, 用相同的算法, 相同的手段去进行摘要, 获得的值总是相同的

# md5是一个算法, 32位的字符串, 每个字符串都是一个十六进制
# md5算法 效率快 算法相对简单

# s1 = "alex3714"
# md5_obj = hashlib.md5()
# md5_obj.update(s1.encode("utf-8"))
# ret = md5_obj.hexdigest()
# print(ret,len(ret),type(ret))

# 数据库 - 撞库

# s1 = "123456"
# md5_obj = hashlib.md5()
# md5_obj.update(s1.encode("utf_8"))
# res = md5_obj.hexdigest()
# print(res)  # e10adc3949ba59abbe56e057f20f883e

# 加盐
# s1 = "alex7314"
# md5_obj = hashlib.md5("r任意的字符串作为盐".encode("utf-8"))
# md5_obj.update(s1.encode("utf-8"))
# res = md5_obj.hexdigest()
# print(res)  # a84659b69fe3abbafc250e9d56ed47a5

# 动态加盐
# username = input("username: ")
# passwd = input("password: ")
# md5_obj = hashlib.md5(username.encode("utf-8"))
# md5_obj.update(passwd.encode("utf-8"))
# print(md5_obj.hexdigest())
# 94e4ccf5e2749b0bfe0428603738c0f9


# sha1也是一个算法, 40位的字符串, 每个字符都是一个十六进制
# 算法相对复杂 计算速度也慢
# s1 = "123456"
# md5_obj = hashlib.sha1()
# md5_obj.update(s1.encode("utf-8"))
# res = md5_obj.hexdigest()
# print(res)

# 文件的一致性校验
# md5_obj = hashlib.md5()
# with open("05.序列化模块_shelve.py.bak","rb")as f:
#     md5_obj.update(f.read())
#     ret = md5_obj.hexdigest()
#     print(ret)
# md5_obj = hashlib.md5()
# with open("05.序列化模块_shelve.py.","rb")as f:
#     md5_obj.update(f.read())
#     ret2 = md5_obj.hexdigest()
#     print(ret2)

# 如果这个文件特别大, 内存装不下
# 按照字节读取

# md5_obj = hashlib.md5()
# md5_obj.update("hello,alex,sb".encode("utf-8"))
# print(md5_obj.hexdigest())
# 6557c9e1d6fc95bf2b12e36c09e13c46

# md5_obj = hashlib.md5()
# md5_obj.update("hello,".encode("utf-8"))
# md5_obj.update("alex,".encode("utf-8"))
# md5_obj.update("sb".encode("utf-8"))
# print(md5_obj.hexdigest())

# 大文件的已执行校验

# md5_obj = hashlib.md5()
# with open("05.序列化模块_shelve.py.bak","rb")as f:
#     md5_obj.update(f.read())
    # 循环的读取文件内容
    # 循环的来update
# print(md5_obj.hexdigest())

# 写成一个函数
# 参数: 文件1的路径, 文件2的路径, 默认参数 = 1024000
# 计算这两个文件的md5值
# 返回他们的一致性结果 T/F

# md5_obj = hashlib.md5()
