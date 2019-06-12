# struct
#

# import struct
# ret = struct.pack("i",2049)    # "i" 代表int, 就是即将要把一个数字转换成国定长度的 bytes 类型
# print(ret)
#
# num = struct.unpack("i",ret)
# print(num)
# print(num[0])

# 如果发送数据的时候
# 先发送长度 先接受长度


import socket
import struct
sk = socket.socket()
sk.bind(("127.0.0.1",8080))
sk.listen()

conn,addr = sk.accept()
while 1:
    cmd = input(">>>")
    if cmd == "q":
        conn.send(b"q")
        break
    conn.send(cmd.encode("gbk"))
    num = conn.recv(4)
    num = struct.unpack("i",num)[0]
    res = conn.recv(int(num)).decode("gbk")
    print(res)

conn.close()
sk.close()

# 我们在网络上传输的所有数据, 都叫数据包
# 数据包里的所有数据, 都叫报文
# 报文里不止有你的数据    ip地址 mac地址 端口号
# 所有的报文都有 报头
# 协议 报头 接受多少个字节
# 我自己定制报文
    # 比如说, 复杂的应用上就会用到
    # 传输文件的时候就够复杂了
        # 文件的名字
        # 文件的大小
        # 文件的类型
        # 存储的路径

head = {"filename":"test","filesize":40960000,"filetype":"txt","filepath":r"E:\编程学习\go\day1"}
# 报头的长度                  # 先接受4个字节
# send(head)    # 报头        # 根据这4个字节获取报头
# send(file)    # 报文        # 从包头中获取filesize, 然后根据filesize接收文件

# 其实, 在网络传输的过程当中, 处处有协议
# 协议就是一堆报文和报头   --字节
# 协议的解析过程我们不需要关心

# 如果跳出我们所了解的端口 ip 协议
# 我们写的程序也需要多次发送数据或者发送多个数据
# 我们也可以自定制协议 -- 本质上就是一种约定
#