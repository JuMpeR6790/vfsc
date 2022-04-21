import threading



class vfsc():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect_to(self, ip, port):
        self.s.connect((ip, port))
          
    def send(self, message):
        self.s.sendall(bytes(message, encoding="utf-8"))

    def listen(self):
        return self.s.recv(1024).decode("utf-8")
    
    

def send_message():   
    while True:
        message = input("chat: ")
        v.send(message)

def receive_message():
    while True:
        print(v.listen())

v = vfsc()
v.connect_to("192.168.1.95", 17234)
receive = threading.Thread(target=receive_message)
receive.start()
send_message()
