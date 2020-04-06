#Método de Gauss
from fractions import Fraction
equations = []
#funcao para imprimir o sistema de equações
def show(equations,unknowns):
  for i in range(unknowns): 
    for j in range(unknowns):
      if(j < unknowns - 1):
        print(equations[i][j], end="x" + str(j+1) + " + ")
      else:
        print(equations[i][j], end="x" + str(j+1))
    print(" = ", equations[i][j+1])
  return 0
#encontra o maior valor - pivoteamento
def highestValue(equations, n, i, j):
  maxValue = 0 #variável que armazenará maior valor da primeira coluna
  lineAux = 0 #variável que armazenará a linha do maior valor
  current = 0 #armazena o valor atual
  ''' buscando o maior valor da primeira coluna '''
  for line in range(i, n):
    for column in range(j, i+1):
      if line == i: 
        maxValue = equations[line][j] 
        lineAux = line
      else:
        if equations[line][j] < 0: 
          current = equations[line][j] * -1
        else:
          current = equations[line][j]
        if maxValue < current:
          maxValue = equations[line][j]
          lineAux = line
  return swapEq(equations,n,lineAux, i, j)  
#troca equação  
def swapEq(equations, n, lineAux, i, j):
  ''' Realizando a troca da linha que possui o maior valor'''
  for line in range(n):
    for column in range(n+1):
      if line == lineAux:
        unknowns_aux = equations[i][column]
        equations[i][column] = equations[line][column]
        equations[line][column] = unknowns_aux
  print("\n\t->->->Equação com maior elemento em módulo->->->")
  return show(equations, n)
#Zera incognita
def makeNull(L1, L):
  if L1 == 0:
    return 0
  constant = (L) / (L1)
  return Fraction(constant).limit_denominator()
def columnResolver(equations, line, column, x):
  for i in range(0, line+1):
    equations[i][column] = equations[i][column] * x
  return equations
def resolve(equations,n, m, length,i):
  if n == 0:
    aux = equations[n][length]
    i = 1
    while i < length:
      aux = aux + (-1 * equations[n][i])
      i+=1
    equations[n][m] = aux / equations[n][m]
    return 0
  if n == length - 1:
    equations[n][length-1] = Fraction(equations[n][length] / equations[n][length-1]).limit_denominator()
    x = equations[n][length-1]
    columnResolver(equations, n-1, length-1, x)
    return resolve(equations, n-1, m, length, i)
  else:
    if n == m:
      aux = equations[n][length]
      i = n + 1
      while i < length:
        aux = aux + (-1 * (equations[n][i]))
        i+=1 
      equations[n][m] = aux / equations[n][m]
      x = equations[n][m]
      columnResolver(equations, n-1, m, x)
      return resolve(equations, n-1, m - 1, length, i)
    elif m > 0:
      return resolve(equations, n, m-1, length, i)
    else:
      return resolve(equations, n-1, 2, length, i)
#verifica se a última equação possui apenas uma incognita
def checkEquation(equations, n):
  if(equations[n-1][n-2] == 0):
    return True
  else:
    return False
#controladora de pivoteamento
def pivotController(equations, n, i, j):
    highestValue(equations, n, i, j)
    if(checkEquation(equations, n) == False):
      for line in range(i+1, n):
        k = makeNull(equations[i][j], equations[line][j])
        for column in range(j, n+1):
          equations[line][column] = equations[line][column] - (k * equations[i][column])
      return pivotController(equations, n, i+1, j+1)
    else:
      return resolve(equations, n-1, n-1, n, 0)
      return 0
    return 0
#controladora principal
def main():
  print("Método de Gauss - Programa")
  unknowns = int(input("Número de incógnitas: "))
  #preenche o sistema de equação
  for i in range(unknowns):
    line = []
    for j in range(unknowns):
      print("Digite o valor de x"+ str(j+1))
      line.append(int(input("-> ")))
    line.append(int(input("Digite a equidade -> ")))
    equations.append(line)
  print("\n")
  print("\t\t\t Sua equação ")
  show(equations, unknowns)
  pivotController(equations, unknowns, 0, 0)
  print("\n\n\t ->->-> Resultado ->->->")
  for i in range(unknowns):
    for j in range(unknowns):
      if i == j:
        print("x" + str(i+1), "=", equations[i][j])
main()
