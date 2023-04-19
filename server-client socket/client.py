"""
    Soket programlama, birbiriyle iletişim kurmak için bir ağ üzerindeki iki düğümü bağlamanın bir yoludur. 
    Bir soket (düğüm), bir IP'deki belirli bir bağlantı noktasını dinlerken, diğer soket bir bağlantı oluşturmak için diğerine ulaşır.
    İstemci sunucuya ulaşırken sunucu dinleyici soketini oluşturur. client.py & server.py dosyalarında bu soket programlama uygulanmıştır.
"""

import socket

HEADER  = 64
PORT = 4444
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"  
SERVER = socket.gethostbyname(socket.gethostname())
ADDR =(SERVER,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Hello!") 
input()
send(DISCONNECT_MESSAGE)
