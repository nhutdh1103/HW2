#import socket module

from fileinput import filename
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a sever socket
#Fill in start
HOST = '10.251.37.23'
PORT = 1103
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)
print(f'the web server is up on port: {HOST}:{PORT}')

#Fill in end
while True:
#Establish the connection 
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split() [1]
        f = open(filename[1:])
        outputdata = f.read()

        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send(bytes('HTTP/1.1 200 OK', 'UTF-8'))
        # connectionSocket.send(bytes(outputdata,'UTF-8'))

        #Fill in end
        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        #Fill in start
        connectionSocket.send(bytes('HTTP/1.1 404 Not Found', 'UTF-8'))
        
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

serverSocket.close()
sys.exit()  #Terminate the program after sending the corresponding data



