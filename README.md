# VFSC
VFSC (very fancy socket communicator) is a very simple (but fancy) python api to create simple chat clients (text only). 

# How to use it?

Linux/macOS:

First, if you want to host a VFSC server, simply download the init.py file, place the file in a folder and run the init.py using python3 init.py. It will generate all necessary files for the server. When it is done, run the the server.py file.

To download init.py using a terminal:  wget -O init.py https://raw.githubusercontent.com/JuMpeR6790/vfsc/main/init.py

Windows:

If you are on Windows, the init.py won't work, it should soon be working but until it does, you can try doing the setup manually by manually installing in a folder the server.py file, and inside that sazme folder, create a logs.txt and config file.


To make a client, please check the documentation and the demo client.

# Server commands:

stop : used to stop the server and close all connections

# Client library:

-connect_to(ip, port) : ip should be a string and port an int, Used to connect to the server


-send(message) : message should be a string, Used to send a string to the server


-listen() : Stores the last message sent to the server


For more info check the client.py file.
