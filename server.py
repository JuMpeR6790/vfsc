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
list_of_conn = []
main_loop = True
print("Starting [...]")

    

def start_server():
    global number_connections
    number_connections = 0
    s.bind((SERVER_IP, PORT))
    print("Server up!")
    print("port:", PORT)
    print("ip:", SERVER_IP)
    print("logs:", LOGS)
    commandThread = threading.Thread(target=commands)
    commandThread.start()
    s.listen(1)
    while main_loop:
        conn,addr = s.accept()
        clients = threading.Thread(target=connections, args=(conn,addr))
        clients.start()
        number_connections = number_connections + 1
        if number_connections == 1:
            print(number_connections, "client connected")
        else:
            print(number_connections, "clients connected")

        
def connections(conn,addr):
    list_of_conn.append(conn)
    print("Connected to ", addr)
    while main_loop:
        message = conn.recv(1024).decode("utf-8")
        if message == "":
            s.close
            number_connections = number_connections - 1
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
            disconnect()
            main_loop = False
            sys.exit
            print("You can safely control + c to terminate the server")
            break
        elif command == "list":
            print(list_of_conn)
        else:
            print("Unknown command")
        
def echo_messages(message):
    for i in list_of_conn:
        i.sendall(bytes(message, encoding="utf-8"))

def disconnect():
    for i in list_of_conn:
        i.close()

start_server()
