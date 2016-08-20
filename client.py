#coding = utf-8

import socket
import threading

class UdpServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.address = ('127.0.0.1', 10001)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(self.address)
        self.stop_flag = False
             
        
    def recieve_msg(self):
        (data, addr) = self.s.recvfrom(2048)
        if data:
            print 'recieve data from', addr
            print data
            
    def run(self):
        while not self.stop_flag:
            self.recieve_msg()
            
    def stop(self):
        self.stop_flag = True
            
class UdpClient(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.address = ('127.0.0.1', 10000)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.stop_flag = False
        
    def send_msg(self):
        data = raw_input()
        if not data:
            print 'Wrong inpiut'
            return
        else:
            self.s.sendto(data, self.address)

        
    def run(self):
        while not self.stop_flag:
            self.send_msg()
        
    def stop(self):
        self.stop_flag = True
            
            
def main():
    t1 = UdpServer()
    t2 = UdpClient()
    t1.start()
    t2.start()
                
                
                
if __name__ == '__main__':
    main()