import random
print("Adivinhação")

numero = random.randint(0,5)
print(numero)

x=0
while x < 6:
    usu = int(input("Qual número você acha que o computador pensou? \n"))
    if usu == numero:
        print("Você acertou!!!!")
        x = 10
        
    else:
        print("Você errou!!!!")
        
    x+=1
print("O computador pensou em", numero)

