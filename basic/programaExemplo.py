'Tipos de dados'
#int = 1,2,3,4,5,6 .. 
#float = 1.5, 1.6, 1.7
#char = 'a', 'b', 'c', '1'
#String = 'abc1'

'Prioridades'
#------------------
'Declaração de variáveis'
#nome(String - str),sobrenome(str),telefone(int),sexo(char),cpf(int)
print("Cadastro de cliente")
nome = ""
sobrenome = ""
telefone = 0
sexo = ''
cpf = 0
avaliacao = 0.0
feedback = ""

#receber esses dados
'input'
nome = str(input("Digite seu nome: ")) #o tipo de dado, pede o dado.
sobrenome = str(input("Digite seu sobrenome: "))
telefone = int(input("Digite seu telefone: "))

sexo = str(input("Digite seu sexo: "))
while(not(sexo == 'f' or sexo == 'm')):
  print("-- Você precisa digitar um valor válido! ")
  sexo = str(input("Digite seu sexo: "))

if(sexo=='f' or sexo=='m'):
  print("perfeito!")

cpf = int(input("Digite seu cpf: "))
avaliacao = float(input("De uma nota para nossos bolos: "))
#mostrar esses dados
print("-----------------------------\n\tConfirme seus dados.\n")
print("Olá, "+nome+ " "+sobrenome+ ". \nVocê cadastrou o telefone " +str(telefone)+", \nvocê é do sexo "+sexo+ ", \nseu cpf é "+str(cpf)+ " \ne você nos avaliou com a nota "+str(avaliacao))

if(avaliacao<=5): #se avaliação for menor que 5
  print("Por que tão ruim?\n\t")
  feedback = input("Sua resposta: ")
else: #senão
  print("Agradecemos a sua nota.")

#se sexo for igual a m ou igual a f print("Tudo certo.")
#senão print("Ops, somente pode valer m ou f")







