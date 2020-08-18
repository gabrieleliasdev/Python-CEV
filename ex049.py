"""049 - Refaça o desafio 009, monstrando a tabuada de um número que o usuário escolher.
  Só que agora utilizando um laço for."""

print("\n", "-=-"*10)
n = int(input(" Type a number: "))

for c in range (0, 11):
  print("{} * {:2} = {}".format(n,c,n*c))
print("End")
