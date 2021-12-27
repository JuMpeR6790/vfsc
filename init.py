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
    os.system("rm init.py")   
    

first_run()
