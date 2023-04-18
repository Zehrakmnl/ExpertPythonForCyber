import socket
import threading
# https://realpython.com/python-sockets/

PORT = 4444
#SERVER = "ipconfig ile bulduğumuz ipv4 ip adresi" yazılabilir fakat bu dinamiklikten kaybettirecektir. bu yüzden tavsiye edilmez
SERVER = socket.gethostbyname(socket.gethostname()) # bulunulan cihazın aktif kullanılan ip adresini bize verecektir.
# print(SERVER) ile kontrol edilebilir.
ADDR = (SERVER,PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR) #  içine verilen objeye göre yeni bir fonksiyon kopyası yaratır. Oluşan bu kopya fonksiyonu daha sonradan argüman listesi ile beraber gönderilen objeye kullanabiliriz
