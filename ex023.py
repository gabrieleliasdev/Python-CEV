# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex; Digite um número: 1834 unidade: 4 dezena: 3 centena: 8 milhar: 1

n1 = int(input('\nType a number of 04-digit, ex.: 1834:\n>>> '))

n = str(n1)

print('\nUnity: {} | Ten: {} | Hundred: {} | Thousands: {}\n'.format(n[3], n[2], n[1], n[0]))
