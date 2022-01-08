#Logic: if we can connect to the port it is open
#if we cannot connect to the port it is closed

import socket  #socket is used to connect to the port over internet
from IPy import IP  #for converting domains into IP's

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)  # to make the scanning faster
        sock.connect((ipaddress, port))
        print('[+] Port ' + str(port) + ' is Open')
    except:
        pass
        # print('[-] Port ' + str(port) + ' is Closed')

ip = input('[+] Enter the IP Address: ')
for port in range(1,100):
    scan_port(ip, port)

# port = 80
# scan_port(ip, port)