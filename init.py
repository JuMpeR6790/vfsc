import platform
import os
from configparser import ConfigParser
import socket

currentOS = platform.system() #récupère le système d'exploitation pour adapter le script d'installation 

def first_run_unix():  #pour les ssytème d'exploitation "unix like" comme macOS et toutes les distributions de Linux
    s = socket.gethostname()
    ip = socket.gethostbyname(s)
    os.system("touch logs.txt")       #creér un fichier logs.txt pour sauvergarder tous les messages envoyés au serveur
    config_object = ConfigParser()
    config_object["Settings"] = {
    "ipaddr": str(ip),
    "port": 17212,
    "logs": "on" 
    }
    with open('config.ini', 'w') as conf:    #créer un fichier de configuration avec une option pour chnager l'adresse ip, le port et si l'utilisateur veux utiliser les logs
        config_object.write(conf)  
    os.system("rm init.py") 
    os.system("wget -O server.py https://raw.githubusercontent.com/JuMpeR6790/vfsc/main/server.py")

def first_run_windows():           #meme chose que au dessus mais adapter à windows
    s = socket.gethostname()
    ip = socket.gethostbyname(s)
    open("logs.txt", "a")
    config_object = ConfigParser()
    config_object["Settings"] = {
    "ipaddr": str(ip),
    "port": 17212,
    "logs": "on" 
    }
    with open('config.ini', 'w') as conf:
        config_object.write(conf)  
    os.remove("init.py") 
    os.system("curl https://raw.githubusercontent.com/JuMpeR6790/vfsc/main/server.py -o server.py")


if currentOS == "Windows":     #verification du sytème d'exploitation
    first_run_windows()
else:
    first_run_unix()
