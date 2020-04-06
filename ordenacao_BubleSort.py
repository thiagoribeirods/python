#Algoritmo de ordenação BubleSort

def Bsort(vetor):
  for i in range(len(vetor)-1):
    for x in range (len(vetor)-1):
      if vetor[x] > vetor [x+1]:
        aux = vetor[x]
        vetor[x] = vetor[x+1]
        vetor[x+1] = aux          
  return vetor

usu = int(input("Nº de posições do vetor -> "))
vetor = []
x = 0
while x < usu:
  import random
  vetor.append(random.randint(0,50))
  x+=1

print(vetor)
print(Bsort(vetor))

