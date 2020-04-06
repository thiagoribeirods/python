matriz = [] #declaro um vetor
cont = 0 #esse contador é para imprimir em ordem crescente as posições da matriz
for i in range(3): #laço de repetição para criar a matriz
  linha = [] #esse vetor será as linhas da minha matriz
  for j in range(3):
    linha.append(cont) #adicione em ordem crescente as posições
    cont +=1 #incremento para a próxima posição ser cont + 1
  matriz.append(linha) #Adiciono as linhas da matriz

for i in range(3): #Esse laço imprime a matriz em forma de matriz
  for j in range(3):
    print(matriz[i][j], end=" ")
  print("\n")
