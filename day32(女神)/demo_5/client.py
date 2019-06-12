# 发送端
import  socket
import os
import json
import struct
sk = socket.socket()
sk.connect(("127.0.0.1",8090))
buffer = 4096
# 发送文件
head = {"filepath":r"E:\编程学习\Python\老男孩Python14期\第3部分-网络编程(女神)\day32",
        "filename":r"day32-01  复习~1.mp4",
        "filesize":None}
file_path = os.path.join(head["filepath"],head["filename"])
filesize = os.path.getsize(file_path)
head["filesize"] = filesize
json_henad = json.dumps(head)   # 字典转成字符串
bytes_head = json_henad.encode("utf-8") # 字符串转bytes
# print(json_henad)
# print(bytes_head)
# 计算head的长度
head_len = len(bytes_head)  # 报头的长度
pack_len = struct.pack("i",head_len)
print(head_len,pack_len)
sk.send(pack_len)   # 先发报头的长度
sk.send(bytes_head) # 再发送bytes类型的报头
with open(file_path,"rb") as f:
    while filesize:
        print(filesize)
        if filesize >= buffer:
            content = f.read(buffer)    # 每次读出来的内容
            sk.send(content)
            filesize = filesize - buffer
        else:
            content = f.read(filesize)
            sk.send(content)
            # filesize -= filesize
            break
sk.close()