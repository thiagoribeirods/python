print("Caixa eletrônico")
sacar = float(input("Valor a ser sacado: R$"))
notas100 = sacar//100
notas50 = ((sacar - notas100*100))//50
notas20 = ((sacar - notas100*100) - (notas50*50))//20
notas10 = ((sacar - notas100*100) - (notas50*50) - notas20*20)//10
notas5 = ((sacar - notas100*100) - (notas50*50) - (notas20*20) - (notas10*10))//5
notas2 = ((sacar - notas100*100) - (notas50*50) - (notas20*20) - (notas10*10) - (notas5*5))//2

print("Notas de R$100.....",notas100)
print("Notas de R$50.....",notas50)
print("Notas de R$20.....",notas20)
print("Notas de R$10.....",notas10)
print("Notas de R$5.....",notas5)
print("Notas de R$2.....",notas2)
