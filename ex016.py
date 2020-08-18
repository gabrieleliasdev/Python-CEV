# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc

n = float(input('\nAny number:\n>>> '))

print('Returned the whole number: {}'.format(trunc(n)))
print('Returned the whole number: {}'.format(int(n)))
