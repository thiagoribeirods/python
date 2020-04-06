#Algoritmo de BubleSort

vetor = [50,30,40,20,10]

for i in range(len(vetor)-1):
  for x in range (len(vetor)-1):
    if vetor[x] > vetor [x+1]:
      aux = vetor[x]
      vetor[x] = vetor[x+1]
      vetor[x+1] = aux
      print(vetor)
      
