import queue
q = queue.Queue()
q.put("你好吗")
q.put("wo ")
print(q.qsize())
print(q.get())
print(q.qsize())