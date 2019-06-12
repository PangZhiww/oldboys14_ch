import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 8080))
while 1:
    msg = input(">>>")
    if msg == "q":
        break
    sk.send(("美团: " + msg).encode("utf-8"))
    ret = sk.recv(1024).decode("utf-8")
    print(ret)
sk.close()
