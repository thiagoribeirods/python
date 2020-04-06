notas = []

for i in range(3):
  alunos = []
  for j in range(3):
    alunos.append(float(input(f"Insira as notas do aluno {i+1} -> ")))
  print('\n')
  notas.append(alunos)

for i in range(3):
  print(f"Aluno {i+1}")
  for j in range(3):
    print(notas[i][j], end=" ")
  print("\n")

media = 0
for i in range(3):
  for j in range(3):
    media = media + notas[i][j]
media = media / 9
print("A média é {:.2f}".format(media))
