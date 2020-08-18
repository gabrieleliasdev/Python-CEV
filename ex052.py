"""052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número inteiro."""

n = int(input("\nType a number: "))
tot = 0

for c in range(1, n+1):

  if n % c == 0:
    print('\033[33m', end='')
    tot += 1

  else:
    print('\033[31m', end='')

  print('{} '.format(c), end='')

print("\n\n\033[mThe number {} was disviible {} times".format(n, tot))

if tot == 2:
  print("\nIt's prime number")

else:
  print("\nNot a prime number")

print("\nEnd")


