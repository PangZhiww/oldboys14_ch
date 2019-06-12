# import socket
# #
# # sk = socket.socket()  # 买手机
# # sk.connect(("127.0.0.1", 8898))  # 拨号
# #
# # sk.send(b"hello word")
# # ret = sk.recv(1024)  # 听别人说话
# # print(ret)  # 和别人说话, 必须传一个bytes类型
# # sk.send(bytes("中午吃什么?",encoding=("utf-8")))
# # ret = sk.recv(1024)
# # print(ret.decode("utf-8"))
# # sk.close()


import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 8109))
while True:
    info = input(">>>")
    sk.send(bytes(info, encoding="utf-8"))
    ret = sk.recv(1024).decode("utf-8")
    print(ret)
    if ret == "bye":
        sk.send(b"bye!bye!")
        break
# sk.send(b"hello wold")
# ret = sk.recv(1024)
# print(ret)
sk.close()
