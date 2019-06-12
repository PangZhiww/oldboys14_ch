# socket tcp
# sockerserver tcp
import socketserver
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):   # self.request 就相当于一个conn
        # print(self.request.recv(1024).decode("utf-8"))
        while True:
            print(self.client_address)
            msg = self.request.recv(1024).decode("utf-8")
            if msg == "q":
                # self.request.close()
                break
            print(msg)
            info = input(">>>")
            self.request.send(info.encode("utf-8"))
if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("127.0.0.1",8080),MyServer)
    # thread 线程
    server.serve_forever()


# 看源码的要点
    # 1. 多个类之间的继承关系要先整理
    # 2. 每一个类中有哪些方法, 要大致列出来
    # 3. 所有的self对象调用要清楚地了解 到底是谁的对象
    # 4. 所有的方法调用要退回到最子类的类中开始寻找, 逐级向上