import socket
import subprocess

host = '127.0.0.1'
port = 50001

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host,port))
serverSocket.listen()

conn, addr = serverSocket.accept() # returns 2 value from connections
print("connected from : " +str(addr))

while True:
    data = conn.recv(1024).decode()
    print(data)

    result = subprocess.run(data, stdout=subprocess.PIPE, shell=True)
    if (result.stdout.decode()!=""):
        responseData=result.stdout
    else:
        responseData=("Command Executed ").encode()
    conn.send(responseData)
conn.close()


        
