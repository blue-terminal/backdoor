import socket
import os
import time
while True:
    sockets = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    indirizzo = ('192.168.111.160', 1090)
    utente=input("inserisci comando\n")
    message = os.system(utente)
    print(f'Invio del messaggio: "{message}" a {indirizzo}')   
    sockets.sendto(utente.encode(), indirizzo)
    time.sleep(10)
    sockets.close()

