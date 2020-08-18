"""040 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida.
 - Média abaixo de 5.0: Reprovado
 - Média entre 5.0 e 6.09: Recuperação
 - Média 7.0 ou superior: Aprovado"""

n1 = float(input("\nType the first note: "))

n2 = float(input("\nType the second note: "))

m = (n1 + n2) / 2

if m < 5:
  print("Disapproved")

elif m >= 5 and m <= 6.9:
  print("Recovery")

elif m >= 7:
  print("Aproved")

else:
  print("Erro")
