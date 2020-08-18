"""047 - Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50."""

print("-=-"*10)

for c in range(2, 51, 2):
  print(c, end=" ")
print("End")

print("-=-"*10)

for c in range(2, 51, 2):
  print(".", end=" ")
  if c % 2 == 0:
    print(c, end=" ")
print("End")
