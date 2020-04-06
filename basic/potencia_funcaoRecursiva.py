print("Recursivo")
#recursivo
def recursivo(base,expoente):
  if expoente == 1:
    return base
  elif expoente == 0:
    return 1
  else:
    return base * recursivo(base,expoente-1)

print(recursivo(3,0))

print("Iterativo")
#iterativo
def iterativo(base,expoente):
  potencia = base**expoente
  return potencia
print(iterativo(3,0))
