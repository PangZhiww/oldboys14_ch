# 连续 send 两个小数据
# 两个 recv , 第一个recv 数据体别小
# 远程执行命令的程序
# ipconfig --> 20003
# 2000-1024=976
# dir --> 200
# 200-976 --> 黏包


# 连续 send 两个小数据 2+8=10
    # 2
    # 8
# 两个 recv , 第一个recv 数据体别小
    # recv(数据的长度)
# 本质: 你不知道到底要接收多大的数据

# 解决
# 首先发送一下这个数据到底有多大
# 再按照数据的长度接收数据
#


import socket
sk = socket.socket()
sk.bind(("127.0.0.1",8080))
sk.listen()

conn,addr = sk.accept()
while 1:
    cmd = input(">>>")
    if cmd == "q":
        conn.send(b"q")
        break
    conn.send(cmd.encode("gbk"))
    num = conn.recv(1024).decode("utf-8")
    # print(num)
    conn.send(b"ok!")
    res = conn.recv(int(num)).decode("gbk")
    print(res)

conn.close()
sk.close()

# 好处: 确定了到底要接收多大的数据
    # 要在文件中配置一个配置项: 就是每次recv的大小  buffer = 4096
    # 当我们要发送大数据的时候, 要明确的告诉接收方要发送多大的数据, 一遍接收方能够准确地接收到所有的数据
    # 多用在文件传输的过程当中
        # 大文件的传输, 一定是按照字节读的, 每次固定字节
        # 传输过程中, 一边读一边传, 接收端, 一边收一边写
        # send 这个大文件之前, 35672字节 send(4096) 35672-4096-4096
        # recv 这个大文件, recv 35672字节 recv(2048) 35672-2048-2048

# 不好的地方: 多了一次交互
#  send 和 sendto 在超过一定范围的时候, 都会报错
# 程序的内存管理