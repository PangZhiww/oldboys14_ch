import socket
from socket import SOL_SOCKET,SO_REUSEADDR
sk = socket.socket()
sk.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sk.bind(("127.0.0.1",8080))
sk.listen()
while 1:
    conn,addr = sk.accept()
    data = conn.recv(9000)
    print(data)
    conn.send(b"http/1.1 200 ok\r\n\r\n")
    # conn.send(b'o98k!new 123 wwsa')
    with open("test.html","rb") as f:
        conn.send(f.read())
    conn.close()
sk.close()