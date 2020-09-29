import socket #importa modulo socket
import time
print("""
  o-o o  o   O  o-O-o   o-o o--o       o-o  o--o o--o  o   o o--o o--o  
 /    |  |  / \   |    /    |   |     |     |    |   | |   | |    |   | 
O     O--O o---o  |   O     O--o       o-o  O-o  O-Oo  o   o O-o  O-Oo  
 \    |  | |   |  |    \    |             | |    |  \   \ /  |    |  \  
  o-o o  o o   o  o     o-o o         o--o  o--o o   o   o   o--o o   o \n""")
TCP_IP = '192.168.0.113' # endereço IP do servidor 
TCP_PORTA = 41891    # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024     # definição do tamanho do buffer
 
# Criação de socket TCP
# SOCK_STREAM, indica que será TCP.
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP e porta que o servidor deve aguardar a conexão
servidor.bind((TCP_IP, TCP_PORTA))

#Define o limite de conexões. 
servidor.listen(1)
time.sleep(1)
print("\t\tDados da conexão")
time.sleep(1)
print("ENDEREÇO:",TCP_IP)
time.sleep(1)
print("PORTA:",TCP_PORTA)
time.sleep(1)
print("SOCKET:",servidor)
time.sleep(2)
print("Tudo pronto!")
# Aceita conexão 
conn, addr = servidor.accept()
print ('Endereço conectado:', addr)

quit = False
while quit == False:
    #dados retidados da mensagem recebida
    data = conn.recv(TAMANHO_BUFFER)
    if data:
        if data.decode('UTF-8') == "quit":
            print("Sua conexão foi encerrada. Até mais!")
            break
        print ("Cliente:", data.decode('UTF-8'))
        msg = input("Você: ")
        conn.send(msg.encode('UTF-8')) # envia dados recebidos em letra maiuscula 

