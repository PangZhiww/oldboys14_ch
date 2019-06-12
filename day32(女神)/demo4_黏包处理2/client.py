import struct
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
    len_num = len(std_out)+len(std_err)
    # print(str(len(std_out)+len(std_err)).encode("utf-8"))
    num_bytes = struct.pack("i",len_num)
    sk.send(num_bytes)
    sk.send(std_out)
    sk.send(std_err)

sk.close()
