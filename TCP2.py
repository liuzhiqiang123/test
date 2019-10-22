# import socket
#
# server = socket.socket()
# server.bind(('127.0.0.1',9999))
# server.listen()
#
# s,raddr = server.accept() # 等待对方链接过来
# print(s,raddr)
# data = s.recv(1024) # 1024作为缓冲区的大小
# print(data)
# print(type(data))
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
            f = s.makefile(mode='rw')
            logging.info(raddr)
            logging.info(s)
            logging.info(f)
            self.clients[raddr] = f

            threading.Thread(target=self.recv, name='recv',args=(f,raddr)).start()

    def recv(self,f,addr): # 很多线程
        while not self.event.is_set():
            try:
                #data = sock.recv(1024)
                data = f.readline() # string
                logging.info(data)
            except Exception as e:
                logging.error(e)
                data = 'quit'
            if data == 'quit':
                self.clients.pop(addr)
                f.close()
                break

            msg = "ack{}. {} {}".format(
                addr,
                datetime.datetime.now().strftime("%y/%m/%d-%H:%M:%S"),
                data)

            for s in self.clients.values():
                #s.send(msg)
                f.write(msg)
                f.flush()

    def stop(self):
        for s in self.clients.values():
            s.close()
        self.sock.close()
        self.event.set()

def main():
    cs = ChatServer()
    cs.start()

    while True:
        cmd = input('>>>')
        if cmd.strip() == 'quit':
            cs.stop()
            threading.Event.wait(3)
            break
        logging.info(threading.enumerate())

if __name__ == '__main__':
    main()

