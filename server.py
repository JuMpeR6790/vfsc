import socket 
import threading 
import sys 

PORT = 17564
SERVER_IP = "192.168.1.95"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def start_server():
    number_connections = 0
    print("Starting [...]")
    s.bind((SERVER_IP, PORT))
    print("Server up!")
    commandThread = threading.Thread(target=commands)
    commandThread.start()
    s.listen(1)
    while True:
        conn,addr = s.accept()
        clients = threading.Thread(target=connections, args=(conn,addr))
        clients.start()
        number_connections = number_connections + 1
        print(number_connections, "clients connected")

def connections(conn,addr):
    print("Connected to ", addr)
    connected = True
    while connected:
        message = conn.recv(1024).decode("utf-8")
        print(message)

def commands():
    while True:
        print("Feel free to type commands in the console")
        command = input()
        if command == "stop":
            print("Stopping [...]")
            s.close
            sys.exit
            break
        else:
            print("Unknown command")
           
        

start_server()