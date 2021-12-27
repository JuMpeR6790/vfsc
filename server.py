from os import write
import socket 
import threading 
import sys 
from configparser import ConfigParser
from datetime import datetime

config_object = ConfigParser()
config_object.read("config.ini")
info = config_object["Settings"]
PORT = int(format(info["port"]))
SERVER_IP = str(format(info["ipaddr"]))
LOGS = str(format(info["logs"]))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
list_of_addr = []
print("Starting [...]")



def start_server():
    number_connections = 0
    s.bind((SERVER_IP, PORT))
    print("Server up!")
    print("port:", PORT)
    print("ip:", SERVER_IP)
    print("logs:", LOGS)
    commandThread = threading.Thread(target=commands)
    commandThread.start()
    s.listen(1)
    while True:
        conn,addr = s.accept()
        clients = threading.Thread(target=connections, args=(conn,addr))
        clients.start()
        number_connections = number_connections + 1
        if number_connections == 1:
            print(number_connections, "client connected")
        else:
            print(number_connections, "clients connected")
        



def connections(conn,addr):
    list_of_addr.append(addr)
    print("Connected to ", addr)
    connected = True
    while connected:
        message = conn.recv(1024).decode("utf-8")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        message_with_info = f"{addr} {current_time} : {message}"
        echo_messages(message_with_info)
        print(message_with_info)
        if LOGS == "on":
            log = open("logs.txt", "a")
            log.write("\n")
            log.writelines(message_with_info)
       


def commands():
    while True:
        command = input()
        if command == "stop":
            print("Stopping [...]")
            s.close
            sys.exit
            print("You can safely control + c to terminate the server")
            break
        else:
            print("Unknown command")
           

def echo_messages(data):
    for i in list_of_addr:
        i.sendall(bytes(data, encoding="utf-8"))
        

start_server()
