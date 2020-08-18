""" 075
   Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
   A) Quantas vezes apareceu o valor 9.
   B) Em que posição foi digitado o primeiro valor 3.
   C) Quais foram os números pares.
"""

lst = tuple(int(input('\nDigite o {}º numero: '.format(i+1))) for i in range(4))

print(f"\nThese were the numbers typed » {lst}")

print(f"\nThe number '{lst[0]}' appeared '{lst.count(lst[0])}' times.")

print(f"\nThe {lst[1]} value appeared in the {lst.index(lst[1])+1}th position.")

print("The even numbers typed were:", end=" ")
for n in lst:
    if n % 2 == 0:
        print(n, end=" ")

