#Imports Modules
import socket
import time
import numpy
import cv2
import base64
#Defines Server Values
listensocket = socket.socket()
Port = 7000
maxConnections = 1000
IP = socket.gethostname() #Gets Hostname Of Current Macheine
print(IP)
IPAddr = socket.gethostbyname(IP)

listensocket.bind(('',Port))

#Opens Server
listensocket.listen(maxConnections)
print("Server started at " + IPAddr + " on port " + str(Port))

#Accepts Incomming Connection
while(True):
    (clientsocket, address) = listensocket.accept()
    print("New connection made!")

    running = True
    message1=""
    #Main
    while running:
        message = clientsocket.recv(1024).decode() #Receives Message
        #print(message) #Prints Message
        #Turns On LED
        if not message == "":
            message1=message1+message
        #Closes Server If Message Is Nothing (Client Terminated)
        else:
            
            running = False

    
    fh = open("imageToSave.png", "wb")
    fh.write(base64.b64decode(message1))
    fh.close()
    (clientsocket, address) = listensocket.accept()
    print("ok")
    output="ok"
    message_to_send = output.encode("UTF-8")
    clientsocket.send(message_to_send)
    clientsocket.close()
