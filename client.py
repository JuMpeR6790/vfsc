import socket 

HOST = "192.168.1.95"
PORT = 17564

def start_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("Connected to server!")
    while True:
        text = input("chat:")
        s.sendall(bytes(text, encoding="utf-8"))

start_client()