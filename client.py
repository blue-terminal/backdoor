import socket
import time
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('192.168.111.160', 1090)
    print('ascolto  {} porta {}'.format(*server_address))
    sock.bind(server_address)
    print('attesa')
    data, address = sock.recvfrom(4096)
    print('sei coleggato  {} al indirizzo {}'.format(len(data), address))
    print(data.decode())
#time.sleep(1000)
#sock.close()
#shutdown /t 0