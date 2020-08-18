# Crie um prorgrama que leia o nome completo de uma pessoa e mostre:
# a) O nome com todas as letras maiúscula | b) O nome com todas as letras minúsculas
# c) QUantas letras ao todo(sem considerar espaços | d) Quantas letras tem o primeiro nome

name = str(input('>>> ')).strip()

print(f'\n{name.upper()}\n')

print(f'{name.lower()}\n')

print(f'{len(name) - name.count(" ")}\n')

print(f'{name.find(" ")}\n')

lista = name.split() # >> or <<<

print(f'{len(lista[0])}\n')
