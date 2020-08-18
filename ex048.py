"""048 - Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três
  e que se encontram no intervalo de 1 até 500"""
s = 0
count = 0
for c in range(1, 501, 2):
  if c % 3 == 0:
    print(c, end=" ")
    count += 1
    s += c
print("Sum = {:.2f} and Quat. {}".format(s,count))
