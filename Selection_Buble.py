#Algoritmo SelectionSort

def Bsort(vetor):
  for i in range(len(vetor)-1):
    for x in range (len(vetor)-1):
      if vetor[x] > vetor [x+1]:
        aux = vetor[x]
        vetor[x] = vetor[x+1]
        vetor[x+1] = aux          
  return vetor

def SelectionSort(vetor):
  for i in range(len(vetor)-1):
    j = i+1
    for j in range(i+1,len(vetor)):
     if vetor[j] < vetor [i]:
       aux = vetor[j]
       vetor[j] = vetor[i]
       vetor[i] = aux
  return vetor
       

usu = int(input("Nº de posições do vetor -> "))
vetor = []
x = 0
while x < usu:
  import random
  vetor.append(random.randint(0,100))
  x+=1
escolha = int(input("1 - BubleSort ou 2 - SelectionSort - >"))

print(vetor)
if escolha ==1:
  print(Bsort(vetor))
else:
  print(SelectionSort(vetor))
