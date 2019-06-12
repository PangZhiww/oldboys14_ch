import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
ip_prot = ("127.0.0.1", 8080)
while 1:
    info = input("大哥:")
    info = ("\033[32m来自大哥的消息: %s\033[0m" % info).encode("utf-8")
    sk.sendto(info, ip_prot)
    msg, addr = sk.recvfrom(1024)
    print(msg.decode("utf-8"))
sk.close()
