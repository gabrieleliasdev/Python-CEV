""" 074
    Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
    Depois disso, mostre a listagem de números gerados e também indique o menor e o
    maior valor que estão na tupla.
"""
from random import randint, sample

lst = []

while True:
    if len(lst) != 5:
        bot = randint(0, 6)
        if bot not in lst:
            lst += [bot]
    else:
        break

print("\nTheses were the 5 numbers drawn from 0 to 6 » ", end="")
for c in lst:
    print(c, end=" ")

print(f"\n\nThis is the highest amount drawn » '{max(lst)}' | and is the lowest amount drawn » '{min(lst)}'")

print("End\n")


a = tuple(sample(range(10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')
