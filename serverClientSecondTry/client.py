# how we send message
import socket

host = '127.0.0.1'
port = 50001

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host,port))

message = input(">> ")

while message.lower().strip!="quit":
    if(message!=""):
        clientSocket.send(message.encode())
        data = clientSocket.recv(1024).decode()
        print("Response from Server : " +str(data))
    message = input(">> ")
clientSocket.close()
