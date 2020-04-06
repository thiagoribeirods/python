#Algoritmo SelectionSort
import time
def inicio1(vetor):
    print("/n")
    inicio = time.time()
    b = Bsort(vetor)
    fim = time.time()
    print(b)
    print("Tempo", fim - inicio)
    print("/n")
    
    
def inicio2(vetor):
    print("/n")
    inicio = time.time()
    b = SelectionSort(vetor)
    fim = time.time()
    print(b)
    print("Tempo", fim - inicio)
    print("/n")
   
    
def Bsort(vetor):
    comp = 0
    cont = 0
    for i in range(len(vetor)-1):
        for x in range (len(vetor)-1):
            comp+=1
            if vetor[x] > vetor [x+1]: #< decrescente
                aux = vetor[x]
                vetor[x] = vetor[x+1]
                vetor[x+1] = aux
                cont+=1
    print("Trocas",cont)
    print("Comparaçoes", comp)
    return vetor

def SelectionSort(vetor):
    comp = 0
    cont = 0
    inicio = time.time()
    for i in range(len(vetor)-1):
        j = i+1
        for j in range(i+1,len(vetor)):
            comp+=1
            if vetor[j] < vetor [i]: #> decrescente
                aux = vetor[j]
                vetor[j] = vetor[i]
                vetor[i] = aux
                cont+=1
    print("Trocas",cont)
    print("Comparaçoes", comp)
    return vetor
       

usu = int(input("Nº de posições do vetor -> "))
vetor1 = []
vetor2 = []
x = 0
while x < usu:
  import random
  vetor1.append(random.randint(0,100))
  x+=1

vetor2 = vetor1[:]
inicio1(vetor1)
inicio2(vetor2)

