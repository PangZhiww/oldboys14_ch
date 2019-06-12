# 接收 server 端的命令之后在自己的机器上执行
import socket
import subprocess
sk = socket.socket()
sk.connect(("127.0.0.1",8080))
while 1:
    cmd = sk.recv(1024).decode("gbk")
    if cmd == "q":
        break
    res = subprocess.Popen(cmd,shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    sk.send(res.stdout.read())
    sk.send(res.stderr.read())
sk.close()