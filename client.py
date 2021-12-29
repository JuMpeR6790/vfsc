import vfsc

def simple_client():
    v = vfsc()
    v.connect_to("192.168.1.95", 17224)
    while True:
        message = input("chat: ")
        v.send(message)

simple_client()
