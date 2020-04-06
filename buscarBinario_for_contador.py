import random
def busca_binaria(lista,usu):
    lista.sort()
    primeiro = 0
    cont = 0
    n = len(lista) - 1
    ultimo = len(lista)-1
    for i in range(n):
        meio = (primeiro+ultimo)//2
        if usu == lista[meio]:
            cont += 1
            return cont					
        elif usu > lista[meio]:
            primeiro = meio + 1
            cont += 1
        elif usu < lista [meio]:
            ultimo = meio - 1
            cont += 1
        else:
            print("erro")
    return cont 
qtd = int(input("Quantos termos você quer que seja gerado? "))
x = 0
lista = []
while x < (qtd) :
  lista.append(random.randint(0,100))
  x+=1  
usu = int(input("Escolha um número: "))
n2 = busca_binaria(lista, usu)
n = len(lista)
if n2 > n:
    print("Não achamos.")
else:
    print(f'Foram necessária {n2} comparações.')

