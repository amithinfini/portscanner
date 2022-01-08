#Logic: if we can connect to the port it is open
#if we cannot connect to the port it is closed

import socket  #socket is used to connect to the port over internet
from IPy import IP  #for converting domains into IP's

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)  # to make the scanning faster
        sock.connect((ipaddress, port))
        print('[+] Port ' + str(port) + ' is Open')
    except:
        pass
        # print('[-] Port ' + str(port) + ' is Closed')

target = input('[+] Enter the Target: ')
converted_ip = check_ip(target)

for port in range(79,89):
    scan_port(converted_ip, port)

# port = 80
# scan_port(ip, port)