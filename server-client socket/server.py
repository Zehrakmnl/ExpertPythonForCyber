"""
    Soket programlama, birbiriyle iletişim kurmak için bir ağ üzerindeki iki düğümü bağlamanın bir yoludur. 
    Bir soket (düğüm), bir IP'deki belirli bir bağlantı noktasını dinlerken, diğer soket bir bağlantı oluşturmak için diğerine ulaşır.
    İstemci sunucuya ulaşırken sunucu dinleyici soketini oluşturur. 
    client.py & server.py dosyalarında bu soket programlama uygulanmıştır.
"""
import socket
import threading
# https://realpython.com/python-sockets/

HEADER  = 64
PORT = 4444
#SERVER = "ipconfig ile bulduğumuz ipv4 ip adresi" yazılabilir fakat bu dinamiklikten kaybettirecektir. bu yüzden tavsiye edilmez
SERVER = socket.gethostbyname(socket.gethostname()) # bulunulan cihazın aktif kullanılan ip adresini bize verecektir.
# print(SERVER) ile kontrol edilebilir. 
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # bir soket örneği oluşturduk
    # AF_INET, adres ailesi ipv4'ü ifade eder. SOCK_STREAM, bağlantı yönelimli TCP protokolü anlamına gelir. 
    # Artık bu soketi kullanarak bir sunucuya bağlanabiliriz.
    print("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))

server.bind(ADDR) #  böylece o IP ve bağlantı noktasından gelen istekleri dinleyebilir.

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} conncected")
    connected = True
    while connected:
        msg_lenght =  conn.recv(HEADER).decode(FORMAT) # .recv() bir sunucudan veya bir istemciden gelen verileri almak için
        msg_lenght = int(msg_lenght)
        msg = conn.recv(msg_lenght).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False 
        print(f"[{addr}] {msg}")
    conn.close()
    


def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() #  accept yöntemi, istemciyle bir bağlantı başlatır. -close() bu bağlantıyı kapatır-
        thread =threading.Thread(target=handle_client, args=(conn,addr)) 
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
 

print("[STARTING] server is starting...")
start()


