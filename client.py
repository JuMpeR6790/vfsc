import vfsc
import threading

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
