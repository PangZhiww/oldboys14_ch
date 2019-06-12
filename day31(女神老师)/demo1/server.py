# import socket
# # tcp 协议
# from socket import SOL_SOCKET,SO_REUSEADDR
# sk = socket.socket()    # 买手机, 创建一个socket对象
# sk.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#
# sk.bind(("127.0.0.1", 8080))    # 给server端绑定一个ip和端口
# sk.listen()
# # socketListen = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp)
# # socketListen.SetSocketOption(SocketOptionLevel.Socket, SocketOptionName.ReuseAddress, true)
# conn,addr = sk.accept() # 获取到一个客户端的连接
#                         # 阻塞
# msg = conn.recv(1024)   # 阻塞, 直到收到一个客户端发来的消息
# print("msg")
# conn.send(b"bello")     # 发消息, 不阻塞
#
# conn.close()            # 关闭连接
# sk.close()              # 关闭socket对象, 如果不关闭, 还能继续接收

# import socket
# from socket import SOL_SOCKET, SO_REUSEADDR
#
# sk = socket.socket()
# sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# sk.bind(("127.0.0.1",8910))
# sk.listen()
# conn,addr = sk.accept()
# while True:
#     msg = sk.recv(1024).decode("utf-8")
#     print(msg)
#     if msg == "bye":break
#     info = input(">>>")
#     if info == "bye":
#         conn.send(b"byebye")
#         break
#     conn.send(info.encode("utf-8"))
#
# conn.close()
# sk.close()

import socket
sk = socket.socket()
sk.bind(("127.0.0.1",8080))
sk.listen()
while 1:
    conn,addr = sk.accept()
    while 1:
        msg = conn.recv(1024).decode("utf-8")
        print(msg)
        if msg == "bye":break
        info = input(">>>")
        if info == "bye":
            conn.send(b"bye")
            break
        conn.send(info.encode("utf-8"))
    conn.close()
sk.close()
