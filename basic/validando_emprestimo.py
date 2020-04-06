print("Aprovação de empréstimo")
casa = float(input("Valor da casa: R$" ))
salario = float(input("Seu salário: R$"))
anos = int(input("Quantidade de anos: "))

mensal = casa/(anos*12)
porcent = salario * 0.3

if mensal > porcent:
    print("Empréstimo nãoo realizado! \nVocê não vai conseguir o empréstimo porque excede seu orçamento de 30%. \n")
    print("Seu salario é R${:.2f}, o valor mensal das prestações é R${:.2f}".format(salario,mensal))
else:
    print("Empréstimo realizado com sucesso!!!")
    
