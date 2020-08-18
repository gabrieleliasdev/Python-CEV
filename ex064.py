"""
    Crie um programa que leia vários números inteiros pelo teclado.
    O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
    No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""

n = cont = sm = 0
lst = []

n = int(input("Type the number '999' to stop counting!\n>>> "))
while n != 999:
    cont += 1
    sm += n
    lst += [n]
    n = int(input(">>> "))

print("Data » Numbers entered: {} | Your quantity: {} | Sum of values: {}".format(lst, cont, sm))
