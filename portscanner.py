#Logic: if we can connect to the port it is open
#if we cannot connect to the port it is closed

import socket  #socket is used to connect to the port over internet
from IPy import IP  #for converting domains into IP's

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(1.0)  # to make the scanning faster
        sock.connect((ipaddress, port))
        print('[+] Port ' + str(port) + ' is Open')
    except:
        print('[-] Port ' + str(port) + ' is Closed')

ip = input('[+] Enter the IP Address: ')
port = 80
scan_port(ip, port)