import socket 

class vfsc():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect_to(self, ip, port):
        self.s.connect((ip, port))
          
    def send(self, message):
        self.s.sendall(bytes(message, encoding="utf-8"))

    def listen(self):
        return self.s.recv(1024).decode("utf-8")
