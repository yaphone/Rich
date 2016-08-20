#coding = utf-8

import socket

class Client:
    def __init__(self):
        self.address = ('127.0.0.1', 10000)
        
    def udp_client(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            data = raw_input()
            if not data:
                print 'Wrong input'
                break
            else:
                s.sendto(data, self.address)
        s.close()
        
if __name__ == '__main__':
    C = Client()
    C.udp_client()
            