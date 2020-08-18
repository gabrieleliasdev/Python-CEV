# Sorteando uma ordem na lista

from random import shuffle

a1 = str(input('\nName of student 1: '))
a2 = str(input('\nName of student 2: '))
a3 = str(input('\nName of student 3: '))
a4 = str(input('\nName of student 4: '))

lista = [a1, a2, a3, a4]

shuffle(lista)

print('\nThe order of presentation will be: {}.\n'.format(lista))

