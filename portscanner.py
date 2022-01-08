import socket  #socket is used to connect to the port over internet
from IPy import IP  #for converting domains into IP's

def scan(target):
    converted_ip = check_ip(target)
    print('\n[-_O] Scanning Target ' + str(target))
    for port in range(79, 89):
        scan_port(converted_ip, port)

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

target = input('[+] Enter the Target/s separated by , ')

if ',' in target:
    for ip_add in target.split(','):
        scan(ip_add.strip(' '))
else:
    scan(target)