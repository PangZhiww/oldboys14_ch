import socket
sk = socket.socket()
sk.bind(("127.0.0.1",8081))
sk.listen()

conn,addr = sk.accept()
ret1 = conn.recv(2)
ret2 = conn.recv(10)
print(ret1)
print(ret2)

conn.close()
sk.close()

# 不知道客户端发送的数据的长度