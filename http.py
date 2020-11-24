"""
http请求响应演示
"""
from socket import socket

HOST="0.0.0.0"
PORT=8051
ADDR=(HOST,PORT)

sock=socket()
sock.bind(ADDR)
sock.listen(5)

connfd,addr=sock.accept()

data=connfd.recv(1024).decode()
print(data)

# file=open("zhihu.html","rb")
#
# data=file.read()
#
# response = """HTTP/1.1 200 OK
# Content-Type:text/html
#
# {}
#
# """.format(data.decode())
# connfd.send(response.encode())

connfd.close()
sock.close()

