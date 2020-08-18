# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

s = '-=-'*20

n = int(input(f'{s}\nType any number and I will tell you if it is odd or even:\n>>> '))

r = n % 2 #O resto da divisão desse número por 2

if r == 0:
  print(f'{s}\nThis number is even!\n')
else:
  print(f'{s}\nThis number is odd!\n')
