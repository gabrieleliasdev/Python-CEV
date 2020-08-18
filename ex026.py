# Faça um programa que leia uma frase pelo teclado e mostre:
# A) Quantas vezes aparece a letra "A".
# B) Em que posição ela aparece a primeira vez.
# C) Em que posição ela aparece a última vez.

p1 = 'The Lord is my shepherd and I will lack nothing.'

print(f'{p1}')

p = p1.lower()

print('\nThe letter "A" appears {} times, the first in {} and the last in {}.\n'
     .format(p.count("a"),p.find("a"),p.rfind("a")))
