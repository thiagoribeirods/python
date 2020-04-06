import random
import time
def mergeSort(vetor):
  n = len(vetor)
  esquerda = vetor[:n//2]
  direita = vetor[n//2:]

  if n > 1:
    meio = n//2
    for i in range(meio):
      esquerda[i] = vetor[i]
    for j in range(meio, n-1):
      direita[j-meio] = vetor [j]

    mergeSort(esquerda)
    mergeSort(direita)
    merge(vetor,esquerda,direita)
    return vetor 

def merge(vetor, esquerda, direita):
  nE = len(esquerda)
  nD = len(direita)
  i = 0
  j = 0
  k = 0
  while i< nE and j < nD:
    if esquerda[i] <= direita [j]:
      vetor[k] = esquerda [i]
      i+=1
    else:
      vetor[k] = direita[j]
      j+=1
    k+=1
  while i < nE:
    vetor[k] = esquerda[i]
    i+=1
    k+=1
    while j < nD:
      vetor[k] = direita [j]
      j+=1
      k+=1
      
def main():
  escolha = int(input("Tamanho do vetor -> "))
  x = 0
  vetor = []
  while x < escolha:
    vetor.append(random.randint(0,100))
    x+=1
  print(vetor)
  a = mergeSort(vetor)
  print("Enviando seu vetor...")
  time.sleep(2)
  print("Contando o número de posições.")
  time.sleep(2)
  print("Organizando...")
  time.sleep(2)
  print("Seu vetor organizado: ")
  time.sleep(1.5)
  print(a)

main()
