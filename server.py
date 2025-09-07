from threading import Thread
import socket

def Send(client):
    while True:
     msg = input("->")
     msg = msg.encode("utf-8")
     client.send(msg)
def Reception(client):
    while True:
     requete_client = client.recv(500)
     requete_client = requete_client.decode('utf-8')
     print(requete_client)
     if not requete_client :
        print("CLOSE")
        break

Host ="0.0.0.0"
Port = 6390


socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.bind((Host,Port))
socket.listen(1)


client,ip =socket.accept()
print("Le client d'ip",ip,"s'est connecter")

envoi = Thread(target=Send,args=[client])
recep = Thread(target=Reception,args=[client])

envoi.start()
recep.start()

recep.join()

client.close()
socket.close()    