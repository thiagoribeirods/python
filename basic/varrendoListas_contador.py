import random
def search(lista,usu):
  n = len(lista)
  cont = 0
  for i in range(n):
    if lista[i] == usu:
      cont+=1
  return cont



qtd = int(input("Quantos termos você quer que seja gerado? "))
x = 0
lista = []
while x < (qtd) :
  lista.append(random.randint(0,10))
  x+=1
usu = int(input("Escolha um número: "))
n = search(lista, usu)

print(f'foram encontradas {n} ocorrencias')
print(lista)n
