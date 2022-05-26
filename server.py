from os import write
import socket 
import threading 
import sys 
from configparser import ConfigParser
from datetime import datetime

sys.tracebacklimit = 0  #pour que python ignore une erreur
config_object = ConfigParser()
config_object.read("config.ini")
info = config_object["Settings"]
PORT = int(format(info["port"]))
SERVER_IP = str(format(info["ipaddr"]))
LOGS = str(format(info["logs"]))
DEBUG = "False"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
list_of_conn = []
main_loop = True
print("Starting [...]")
global number_connection
number_connections = 0
    

def start_server():


    s.bind((SERVER_IP, PORT))
    print("Server up!")
    print("port:", PORT)
    print("ip:", SERVER_IP)
    print("logs:", LOGS)
    commandThread = threading.Thread(target=commands)
    commandThread.start()
    s.listen(1)
    if DEBUG == "True":
        debugThread = threading.Thread(target=debugging)
        debugThread.start()
    while main_loop:
        conn,addr = s.accept()
        clients = threading.Thread(target=connections, args=(conn,addr))
        clients.start()


        
def connections(conn,addr):
    list_of_conn.append(conn)
    print("Connected to ", addr)
    while main_loop:
        message = conn.recv(1024).decode("utf-8")
        if message == "":         #PB ICI TROUVER UN MOYEN DE VERIFIER LA DECONNECTION DU CLIENT              
            print("A client disconnected")
            list_of_conn.remove(conn)
            
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        message_with_info = f"{current_time} {message}"
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
            print("Ctrl + C to exit [...]")
            exit()


        elif command == "list":
            print(list_of_conn)
        else:
            print("Unknown command")
        
def echo_messages(message):
    for i in list_of_conn:
        i.sendall(bytes(message, encoding="utf-8"))

def debugging():
    while True:
        print(list_of_conn)

def disconnect():
    for i in list_of_conn:
        i.shutdown(socket.SHUT_RDWR)
    s.close

start_server()


