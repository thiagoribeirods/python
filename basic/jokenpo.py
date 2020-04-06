import random
print("Jokenpô´")
#pedra = 1
#papel = 2
#tesoura = 3
computador = random.randint(1,3)
x = True
while x == True:
    usu = int(input("Pedra - 1 \nPapel - 2 \nTesoura - 3 \nEscolha: "))
    if usu == 1 and computador == 1 or usu==2 and computador == 2 or usu == 3 and computador ==3:
        print("Empate")
        computador = random.randint(1,3)
        x = True
    elif usu == 1  and computador == 2:
        print("O computador jogou papel")
        print("Você perdeu!!!")
        x = False
    elif usu == 1 and computador == 3:
        print("O computador jogou tesoura")
        print("Você ganhou!!!")
        x = False
    elif usu == 2 and computador == 1:
        print("O computador jogou pedra")
        print("Você ganhou!!!")
        x = False
    elif usu == 2 and computador ==3:
        print("O computador jogou tesoura")
        print("Você perdeu!!!")
        x = False
    elif usu == 3 and computador ==1:
        print("O computador jogou pedra")
        print("Você perdeu!!!!")
        x = False
    elif usu==3 and computador == 2:
        print("O computador jogou papel")
        print("Você ganhou!!!!")
        x = False
    else:
        print("Digite um valor válido!")
        x = True
        
    
    

