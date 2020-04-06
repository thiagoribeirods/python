import random
def search(lista,usu):
  n = len(lista)
  for i in range(n):
    if lista[i] == usu:
      return True
  return False



qtd = int(input("Quantos termos você quer que seja gerado? "))
x = 0
lista = []
while x < (qtd) :
  lista.append(random.randint(0,53))
  x+=1
usu = int(input("Escolha um número: "))
n = search(lista, usu)
if n:
  print("Vc achou!")
else:
  print("puxa, n foi dessa vez")
print(lista)
