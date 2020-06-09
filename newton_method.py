def msg():
  print("\t\t\t ---- Método de Newton ----")
  return 0

def mostrar_pontos(x, y, n):
  print("\t\t --- Mostrando pontos --- ")
  for i in range(n):
    print("-> f(" + str(x[i]) + ") =", str(y[i]))
  return 0

def calcula_ordem(x,y,n, desc):
  #insiro a primeira ordem com os valores de y na primeira coluna
  an = []
  k = 0
  while k < n:
    j = 0
    linha = []
    while j < n:
      if(j < 1):
       linha.append(y[k])
      else:
        linha.append(0)
      j+=1
    an.append(linha)
    k+=1
  #crio uma variavel de ordem para capturar an
  ordem = 1
  #variável incrimento para inserir em an
  x_incremento = 0
  #controla divisor 
  a = 0
  while ordem < n:
    #controlo dentro de uma matriz, a primeira linha conterá os resultados das ordens a0,a1,a2...an 
    an[x_incremento][ordem] = (an[a+1][ordem-1] - an[a][ordem-1]) / ((x[a+ordem]) - (x[a]))
    a+=1
    x_incremento+=1
    #para evitar divisão por zero, paramos sempre que chegarmos no limite do algortimo, nesse caso, cada ordem tira uma linha da matriz
    if(x_incremento == n-ordem):
      x_incremento = 0
      ordem+=1
      a = 0 
  #retorna função que calcula ponto da equação, utilizando a definiçao Pn(x) = a0 + a1(x - x0) ... + an(x-x0) + (...) + an(x-xn-1)
  return pn(an, n, desc, x)

def pn(an, n, desc, x):
  resultado = an[0][0] #insiro o primeiro termo no resultado para facilitar
  for i in range(1,n):
    produtorio = 1
    inc = 0
    while inc < i: #faço somatório de (x - x0)* (...)*(x-xn-1), por isso para quando for igual a i 
      produtorio = produtorio * (desc - x[inc])
      inc+=1
    resultado = resultado + an[0][i] * produtorio
  return resultado


def main():
  msg()
  #pega número de pontos
  n = int(input("Quantidade de X -> "))
  print("\n \t ->-> Inserindo pontos ... ")
  x = []
  y = []
  #insere valor de X
  for i in range(n):
    print("Valor de x" + str(i))
    x.append(int(input(" -> ")))
  #insere valor de f(x)
  print("\t\t --- Inserindo pontos de F(x) --- ")
  for i in range(n):
    print("Valor de f(" + str(x[i]) + ")")
    y.append(int(input(" -> ")))
  desc = float(input("\n ---> Digite o ponto que você deseja encontrar: "))
  #exibe pontos inseridos
  mostrar_pontos(x,y,n)
  resultado = calcula_ordem(x,y,n, desc)
  print("\t\t\t ---- Exibindo resultado ---- \n -> f(" + str(desc)+") =", resultado)
  return 0

main()
