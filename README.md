## VFSC
VFSC (very fancy socket communicator) is a very simple (but fancy) python api to create simple chat clients for beginners. 

# How to download the server 

Linux/macOS:

First, if you want to host a VFSC server, simply download the init.py file, place the file in a folder and run the init.py using python3 init.py. It will generate all necessary files for the server. When it is done, run the the server.py file.

Or simply use the command bellow:

```wget -O init.py [https://raw.githubusercontent.com/JuMpeR6790/vfsc/main/init.py && python3 init.py](https://raw.githubusercontent.com/JuMpeR6790/vfsc/rewrite/init.py)```

Windows:

Same instructions but use the command below:

```curl https://raw.githubusercontent.com/JuMpeR6790/vfsc/main/init.py -o test.py```

# Server commands:

stop : used to stop the server and close all connections

# How to make a client

To make a client, please check the documentation and the demo client.

# Client library:

-connect_to(ip, port) : ip should be a string and port an int, Used to connect to the server


-send(message) : message should be a string, Used to send a string to the server


-listen() : Stores the last message sent to the server


For more info check the client.py file.


# FAQ

Where is the pypi vfsc package? The reason I didn't add any package is that I don't want to make the client installation more complicated by forcing users to download the package.


