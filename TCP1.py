# # 导入包
# import socket
#
# # 创建socket对象
# server = socket.socket()
# # 绑定服务器ip及端口号
# server.bind(('127.0.0.1',9999))
# # 监听等待对方链接过来
# server.listen()
# # 阻断，s是服务器的子socket，raddr是客户端的ip及端口号
# s,raddr = server.accept()
# print('s是',s,type(s))
# print('raddr是',raddr)
# # 接受客户端的byte类型，1024作为缓冲区的大小
# data = s.recv(1024)
# print(data)
# print(type(data))
# # 服务端向客户端发送返回值
# s.send('ask. {}'.format(data.decode()).encode())
#
# s.close()
#
# server.close()
"""
前一小时实现接受多个客户端，并保持链接

"""
import socket
import threading
import logging
import datetime

FORMAT = "%(asctime)s %(threadName)s %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

# TCP Server
class ChatServer:
    def __init__(self,ip='127.0.0.1',port=9999):
        self.addr = (ip,port)
        self.sock = socket.socket()
        self.clients = {}
        self.event = threading.Event()

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen() # 服务启动了

        threading.Thread(target=self.accept, name='accept').start()

    def accept(self):
        while not self.event.is_set(): # 一个线程
            s,raddr = self.sock.accept() # 阻塞
            logging.info(raddr)
            logging.info(s)
            self.clients[raddr] = s

            threading.Thread(target=self.recv, name='recv',args=(s,)).start()

    def recv(self,sock:socket.socket): # 很多线程
        while not self.event.is_set():
            try:
                data = sock.recv(1024)
                logging.info(data)
            except Exception as e:
                logging.error(e)
                data = b'quit'
            if data == b'quit':
                self.clients.pop(sock.getpeername())
                socket.close()
                break

            msg = "ack{}. {} {}".format(
                sock.getpeername(),
                datetime.datetime.now().strftime("%y/%m/%d-%H:%M:%S"),
                data.decode()).encode()

            for s in self.clients.values():
                s.send(msg)

    def stop(self):
        for s in self.clients.values():
            s.close()
        self.sock.close()
        self.event.set()

cs = ChatServer()
cs.start()

while True:
    cmd = input('>>>')
    if cmd.strip() == 'quit':
        cs.stop()
        threading.Event.wait(3)
        break
    logging.info(threading.enumerate())

