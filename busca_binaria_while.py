import random

def busca_binaria(lista,usu):
    lista.sort()
    primeiro = 0
    ultimo = len(lista)-1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo)//2
        if usu == lista[meio]:
            return meio
        elif  usu < lista[meio]:
            ultimo = meio - 1
        elif usu > lista[meio]:
            primeiro = meio + 1
        else:
            print("erro")
    return False
          
  
qtd = int(input("Quantos termos você quer que seja gerado? "))
x = 0
lista = []
while x < (qtd) :
  lista.append(random.randint(0,100))
  x+=1
usu = int(input("Escolha um número: "))

n2 = busca_binaria(lista, usu)
if n2 == False:
    print("Não houve ocorrência do número digitado!")
else:
    print(f'O número {usu} está presente na lista.')

print("-------Veja a lista-----------")
print(lista)

