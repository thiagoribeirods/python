def gera_matriz():
  mat = []
  for i in range(3):
    linhas = []
    for j in range(3):
      linha = int(input("Digite -> "))
      if linha > 0:
        linhas.append(1)
      else:
        linhas.append(0)
    mat.append(linhas)
  return mat

def exibe(a):
  for i in range(3):
    for j in range(3):
      print(a[i][j], end=" ")
    print("\n")
  return a

def troca(matriz):
  return 0


def main():
  a = gera_matriz()
  exibe(a)
  

main()
