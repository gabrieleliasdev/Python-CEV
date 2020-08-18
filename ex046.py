"""046 - Faça um programa que mostre na tela um contagem regressiva para o estouro de fogos de artifício,
  indo de 10 até 0, com uma pausa de 1 segundo entre elas."""

from time import sleep

ct = int(input(" "))

for c in range(ct, -1, -1):
  print(c)
  sleep(1)
print("End")
