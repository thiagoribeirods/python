import random
def msg():
  print("Algoritmo de busca sequencial e binária \n")

def busca_sequencial(vetor, usu): #passo o vetor e o numero que o usuário quer buscar
  for x in range(len(vetor)-1): #inicio o laço de repetição
    if vetor[x] == usu: #comparo posição por posição
      return True #Se encontrar, retorna True
  return False #Se não encontrar, retorna False

def busca_binaria(vetor, usu): #Passo o vetor e o numéro para buscar
  primeiro = 0 #defino a primeira posição do vetor como 0
  ultimo = len(vetor) - 1 '''defino o último (última posição) como o tamanho do vetor - 1 (se o vetor tiver 5 posição, vai de 0 a 4,
  então a ultima posição é 5-1 = 4)'''
  vetor.sort() #Ordeno o vetor
  for x in range(len(vetor)-1):
    meio = (primeiro + ultimo) // 2 #somo o primeiro com o último (dá o tamanho do vetor ) e faço divisão exata para capturar o meio
    if usu == vetor[meio]: # se o número a ser buscado for igual ao número do meio do vetor, já retorno
      return True
    elif usu > vetor[meio]: '''Se o número a ser buscado for maior, o primeiro recebe meio + 1, 
    pois imagine esse vetor -> [primeiro, segundo, meio, quarto, quinto, ultimo], se o termo a ser buscado for o Quinto,
    ele é maior que o meio, então, o primeiro = meio + 1, ou seja, a primeira posição agora é a 3 que guarda o QUARTO, 
    volta pro laço e divide novamente para encontrar o meio.'''
      primeiro = meio + 1
    elif usu < vetor[meio]: #Se o número a ser buscado for menor, o último recebe meio -1, pelo processo de lógica inverso do IF anterior.
      ultimo = meio - 1
    else:
      print("\n")
  return False #Se não encontrar, retorna falso
      
def main():
  msg()
  x = 0 #contador para while
  vetor = []
  while x < 10: #Condição de parada
    vetor.append(random.randint(1,100))
    x+=1 #incremento
  print("------MENU------")
  print("1 - BUSCA BINÁRIA \n2-BUSCA SEQUENCIAL")
  escolha = int(input("Escolha -> "))
  if escolha == 1:
    usu = int(input("Escolha um número para buscar -> "))
    c = busca_binaria(vetor, usu) #envio o vetor e o número a ser buscado para a função
    if c == True: #Se verdadeiro, é porque encontrou
      print("Encontrei o termo na lista. Veja a lista ->")
    else:
      print("Não encontrei o termo na lista. Veja:")
  elif escolha == 2:
    usu = int(input("Escolha um número para buscar -> "))
    b = busca_sequencial(vetor, usu) #envio o vetor e o número a ser buscado para a função
    if b == True: #Se verdadeiro, é porque encontrou
      print("Encontrei o termo na lista. Veja a lista ->")
    else:
      print("Não encontrei o termo na lista. Veja:")
  print(vetor)



main()
