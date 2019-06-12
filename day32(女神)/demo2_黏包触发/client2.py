import socket
sk = socket.socket()
sk.connect(("127.0.0.1",8980))

sk.send(b"helloegg")
# sk.send(b"world")
import time
time.sleep(2)
sk.send(b"hi")

sk.close()