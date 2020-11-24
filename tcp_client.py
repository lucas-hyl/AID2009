"""
tcp 循环模型客户端
"""
from socket import *

# 服务端地址
ADDR = ("127.0.0.1",8800)

tcp_socket = socket()
tcp_socket.connect(ADDR)

# 长时间占有服务端
while True:
    data = input(">>")
    if not data:
        break
    tcp_socket.send(data.encode())
    data = tcp_socket.recv(1024)
    print(data.decode())

tcp_socket.close()