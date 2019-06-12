# import socket
# sk = socket.socket()
# sk.bind(("127.0.0.1", 8080))
# sk.send(b"hi")
# ret = sk.recv(1024)
# print(ret)
# sk.close()

import socket
sk = socket.socket()
sk.bind(("127.0.0.1", 8910))
while True:
    msg = input(">>>")
    if msg == "bye":
        sk.send(b"bye")
        break
    sk.send(msg.encode("utf-8"))
    ret = sk.recv(1024).decode("utf-8")
    if ret == "bye":
        print(ret)
        break
    print(ret)
sk.close()