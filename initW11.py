import os
from configparser import ConfigParser
import socket

def first_run():
    s = socket.gethostname()
    ip = socket.gethostbyname(s)
    os.system("touch logs.txt")
    config_object = ConfigParser()
    config_object["Settings"] = {
    "ipaddr": str(ip),
    "port": 17212,
    "logs": "on" 
    }
    with open('config.ini', 'w') as conf:
        config_object.write(conf)  
    os.system("rm initW11.py") 
    os.system("curl https://raw.githubusercontent.com/JuMpeR6790/vfsc/main/server.py -o server.py")
    

first_run()