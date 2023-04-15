
import argparse
import scapy.all as scapy
# scapy documentation   -> pip3 install scapy <- terminalde indirerek kullanım sağkanabilir. 
# https://scapy.readthedocs.io/en/latest/
class ARP_ping():
    def __init__(self):
        print("ARP ping started !")

    def user_get_input(self):
        
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--interface', type=str, help="Please chose a interface")
        args = parser.parse_args() # kullanım amacı?
        # print(args.interface)
        if args.interface == None:
            print("Enter a valid interface")

    
    def arp_request(self,ip):
        ans, unans = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst="192.168.1.0/24"), timeout=2)
        
    # BU DOKUMANTASYONA BAKARAK ALTERNATIF OLUSTURUYORUZ. TEK SATIRI AÇIYORUZ 

    def ALTERNATIVEarp_request(self,ip):
        
        arp_request_packet = scapy.ARP(pdst=ip)
        broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        combined_packet = broadcast_packet/arp_request_packet

        ans, unans = scapy.srp(combined_packet, timeout=2)
        # / işareti ile iki paket birleştiriliyor. Biz de combined_packet adı ile birleştiriyoruz.   

    def netdiscover(self,ip):
        
        arp_request_packet = scapy.ARP(pdst=ip)
        broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        combined_packet = broadcast_packet/arp_request_packet
        #ans, unans = scapy.srp(combined_packet, timeout=2)
        # ans => cevap listesi 
        # unans => cevaplanmayan liste
        (answered_list,unanswared_list) = scapy.srp(combined_packet, timeout=2)
        answered_list.summary() # özetini verir.

# ARPping sınıfından obje oluşturuyoruz burada
if __name__ == "__main__":
    # kodlarımız import edilmiş mi yoksa asil kod(bu durumda main olur) mu onu belirtir.
    # import edildiyse kod adı main olarak kayıt edilmez
    arpPing = ARP_ping()
    userInput = arpPing.user_get_input()
    arpPing.arp_request(userInput.interface)
    # userInput.interface kullnıcının girdiği ip aralığını veriyor 

