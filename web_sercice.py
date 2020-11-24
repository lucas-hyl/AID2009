"""
web server 程序
"""
from socket import *
from select import *
import re


class WebServer:
    def __init__(self, *, host='0.0.0.0', port=80, html=None):
        self.host = host
        self.port = port
        self.html = html

        self.create_socket()
        self.bind()

        self.rlist = []
        self.wlist = []
        self.xlist = []

    def create_socket(self):
        self.sock = socket()
        self.sock.setblocking(False)

    def bind(self):
        self.address = (self.host, self.port)
        self.sock.bind(self.address)

    # 连接客户端
    def connect(self, sockfd):
        connfd, addr = sockfd.accept()
        print("Connect from", addr)
        # 连接一个客户端就多监控一个
        connfd.setblocking(False)
        self.rlist.append(connfd)

    def handle(self, connfd):
        request = connfd.recv(1024 * 10)
        print(request.decode())
        re = request.decode().split(" ")
        if re[1] == '/index.html':
            file = open("index.html")
            data = file.read()
            response = """HTTP/1.1 200 OK
            Content-Type:text/html

            {}

            """.format(data)
            connfd.send(response.encode())

        # f = open(request)
        # print(f.readline())

    # 启动网络服务
    def start(self):
        self.sock.listen(5)
        self.rlist.append(self.sock)
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sock:
                    self.connect(r)
                else:
                    try:
                        self.handle(r)
                    except:
                        pass
                    finally:



def main():
    web = WebServer(host='0.0.0.0', port=8055, html='./zhihu.html')

    web.start()


if __name__ == '__main__':
    main()
