f = open("亵渎",mode="w+",encoding="utf-8")   #  w 操作, 会青空原来的内容   w+ 一般是不用的
# f.seek(0,2)
f.write("今天天气")
f.seek(0)     #  移动光标
s = f.read()
print(s)
f.flush()
f.close()