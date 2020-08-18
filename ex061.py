"""
    Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
    progressão usando a estrutura while.
"""

fn = int(input("Type the first number: "))
r = int(input("Ratio: "))

termo = fn
cont = 1

while cont <= 10:
    print("{} → ".format(termo), end="")
    termo += r
    cont += 1

print("End")
