# import socket
# sk = socket.socket()    # 买手机
# # sk.bind("ip",port_端口号)   # 绑定手机卡
# sk.bind(('127.0.0.1',8898))   # 绑定手机卡   有了手机号
# sk.listen()     # 监听 等着有人给我打电话
# conn,addr = sk.accept()     # 接听别人的电话   connection - 连接, address - 地址
# ret = conn.recv(1024)     # 听别人说话 括号内是1024的整数倍  听别人说多少字节
# print(ret)
# conn.send(b"hello")     # 和别人说话, 必须传一个bytes类型
# conn.close()    # 挂电话
# sk.close()      # 关机


# 加入一条socket配置，重用ip和端口
# import socket
#
# # from socket import SOL_SOCKET,SO_REUSEADDR
# sk = socket.socket()
# sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 就是它，在bind前加     避免服务重启的时候报address already in use
# sk.bind(('127.0.0.1', 8898))  # 把地址绑定到套接字
# sk.listen()  # 监听链接
# conn, addr = sk.accept()  # 接受客户端链接
# ret = conn.recv(1024)  # 接收客户端信息    只能传递1024个字节
# print(ret)  # 打印客户端信息
# conn.send(b'hi')  # 向客户端发送信息   和别人说话, 必须传一个bytes类型
# ret = conn.recv(1024)
# print(ret.decode("utf-8"))
# conn.send(bytes("大碗油皮面加个蛋不要碗!", encoding=("utf-8")))
# conn.close()  # 关闭客户端套接字
# sk.close()  # 关闭服务器套接字(可选)

# send -- recv
# send -- recv
# recv -- send

# 有收必有发, 收发必相等


import socket
from socket import SOL_SOCKET,SO_REUSEADDR

sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET,SO_REUSEADDR, 1)
sk.bind(("127.0.0.1", 8109))
sk.listen()

conn, addr = sk.accept()
print(addr)
while True:
    ret = conn.recv(1024).decode("utf-8")
    if ret == "bye":
        break
    print(ret)
    info = input(">>>")
    conn.send(bytes(info,encoding="utf-8"))
# ret = conn.recv(1024)
# print(ret)
# conn.send(b"hello")
conn.close()
sk.close()

