import socket #importa modulo socket
import time
print("""
 __            ___  __   __      __          ___      ___  ___ 
/  ` |__|  /\   |  /  ` |__)    /  ` |    | |__  |\ |  |  |__  
\__, |  | /~~\  |  \__, |       \__, |___ | |___ | \|  |  |___ 
                                                              
        """)
print("\t ... Procurando servidor ... ")
time.sleep(1.4)
TCP_IP = '192.168.0.113' # endereço IP do servidor 
TCP_PORTA = 41891      # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024

print("Conectando...")
time.sleep(0.5)
print("Conectado!")

# Criação de socket TCP do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conecta ao servidor em IP e porta especifica 
cliente.connect((TCP_IP, TCP_PORTA))
quit = False #condição de parada
while quit == False:
    MENSAGEM  = input("Você: ")
    if MENSAGEM == "quit":
        cliente.send(MENSAGEM.encode('UTF-8'))
        break
    
    # envia mensagem para servidor 
    cliente.send(MENSAGEM.encode('UTF-8'))

    # recebe dados do servidor 
    data, addr = cliente.recvfrom(1024)        

    print ("Servidor:", data.decode('UTF-8'))
print("Sua conexão foi encerrada. Até mais!")
# fecha conexão com servidor
cliente.close()
