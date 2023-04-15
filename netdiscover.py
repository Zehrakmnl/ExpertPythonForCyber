import argparse
import scapy.all as scapy
class ARP_ping():
    def __init__(self):
        print("ARP ping started !")

    def user_get_input(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--ipaddress', type=str, help="Please chose a interface")
        args = parser.parse_args() 
        print(args.ipaddress)
        if args.ipaddress != None:
           return args
           
    def arp_request(self,ip):
        ans, unans = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=ip), timeout=2)        
if __name__ == "__main__":
    arpPing = ARP_ping()
    userInput = arpPing.user_get_input()
    arpPing.arp_request(userInput.ipaddress)




