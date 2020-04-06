import time
print("Python tintas")

largura = float(input("Largura em metros: "))
altura = float(input("Altura em metros: "))

area = largura * altura
lt_tinta = area/2

print("..........Imprimindo..........")
time.sleep(3)
print(".........Calculando, por favor aguarde!...")
time.sleep(3)
print(".........Quase lá!!!...")
time.sleep(3)
print("Encontrando o pintor..............")
time.sleep(3)
print("O pintor está efetuando as contas, por favor aguarde \n\n\n")
time.sleep(3)
print("{:.1f} litros de tinta são necessários para pintar a parede".format(lt_tinta))

