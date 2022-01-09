import socket  #socket is used to connect to the port over internet
from IPy import IP  #for converting domains into IP's

def scan(target):
    converted_ip = check_ip(target)
    print('\n[-_0] Scanning Target ' + str(target))
    for port in range(1,100):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)  # to make the scanning faster
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open port ' + str(port))
    except:
        pass

target = input('[+] Enter the Target/s(separated by ,): ')

if ',' in target:
    for ip_add in target.split(','):
        scan(ip_add.strip(' '))
else:
    scan(target)