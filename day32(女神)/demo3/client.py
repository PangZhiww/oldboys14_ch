import socket
import subprocess

sk = socket.socket()
sk.connect(("127.0.0.1",8080))
while 1:
    cmd = sk.recv(1024).decode("gbk")
    if cmd == "q":
        break
    res = subprocess.Popen(
        cmd,shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    std_out = res.stdout.read()
    std_err = res.stderr.read()
    # print(str(len(std_out)+len(std_err)).encode("utf-8"))
    sk.send(str(len(std_out)+len(std_err)).encode("utf-8"))
    sk.recv(1024)
    sk.send(std_out)
    sk.send(std_err)

sk.close()
