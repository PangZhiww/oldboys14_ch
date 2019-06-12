import socket
sk = socket.socket()
sk.bind(("127.0.0.1",8980))
sk.listen()
conn,addr = sk.accept()
ret1 = conn.recv(12)
print(ret1)
ret2 = conn.recv(12)
ret3 = conn.recv(12)
print(ret2)
print(ret3)
conn.close()
sk.close()

# windows 会发送一个空消息, 直接报错

# 多个send 小的数据连在一起, 会发生黏包现象, 是tcp协议内部的优化算法造成的
# 连续使用的 send 引起的