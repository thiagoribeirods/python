import math
print("Dobro, triplo e raiz quadrada")

numero = int(input("Digite um número: "))
dobro = numero * 2
triplo = numero * 3
raiz = math.sqrt(numero)

print("O dobro é {}, o triplo é {} e a raiz quadrada é {:.2f}".format(dobro,triplo, raiz))
