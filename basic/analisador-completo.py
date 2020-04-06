print("Analisador completo")
somaidade= 0
maiorH = 0
maiorM = 0
totalMulher20 = 0
nome =""
for pessoa in range(1,5):
    print("---Pessoa ", pessoa," ---")
    pessoa = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F]: "))
    somaidade+=idade
    if pessoa == 1 and sexo in "Mm":
        maiorH = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maiorH:
        maiorh = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totalMulher20+=1
    
    
        
        

media = somaidade/4
print("A média de idade é: ", media)
print("O homem mais velho tem ", maiorH, " e se chama ", nomevelho)
print("São",totalMulher20,"com menos de 20 anos.")

    
    
    
