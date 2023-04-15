# linux terminalinde
# netdiscover -i eth0 -r 10.0.4.0/24 -c 100
# şeklinde bir kod satırı kullandığımızı hatırlayalım.

# terminalden komut almak için kullandığımız bir kütüphane bulunmaktadır. 
# IMPPORT EDILEBILECEK KUTUPHANELER  sys + argparse + 

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--interface', type=str, help="Please chose a interface")
args = parser.parse_args() # kullanım amacı?
print(args.interface)
if args.interface == None:
    print("Enter a valid interface")

