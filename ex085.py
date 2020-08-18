"""
    Exercício Python 085
    Crie um programa onde o usuário possa digitar sete valores numéricos
    e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
    No final, mostre os valores pares e ímpares em ordem crescente.
"""
lst = [[],[]]

for i in range(7):
    i = int(input(f"Type {i+1}ª value » "))
    if i % 2 == 0:
        lst[0].append(i)
    if i % 2 == 1:
        lst[1].append(i)

print(f"\nFollows even values in ascending order » {sorted(lst[0])}")
print(f"\nFollows ood values in ascending order » {sorted(lst[1])}")
