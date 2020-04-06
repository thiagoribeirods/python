import random

def searchLast(lista,usu):
  n = len(lista)
  ultimo = -1
  for i in range(n):
    if lista[i] == usu:
      ultimo = i
  
  
  return ultimo
  
qtd = int(input("Quantos termos você quer que seja gerado? "))
x = 0
lista = []
while x < (qtd) :
  lista.append(random.randint(0,10))
  x+=1
print(lista)
usu = int(input("Escolha um número: "))

n2 = searchLast(lista, usu)

if n2 == -1:
  print('nao houve ocorrencia')
else:
  print('a posicao achada foi',n2)
