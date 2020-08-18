"""
    Exercício Python #082 - Dividindo valores em várias listas
    Crie um programa que vai ler vários números e colocar em uma lista.
    Depois disso, crie duas listas extras que vão conter apenas os valores pares e os
    valores ímpares digitados, respectivamente.
    Ao final, mostre o conteúdo das três listas geradas.
"""
from textwrap import dedent

lst = []
lst1 = []
lst2 = []

while True:
    i = int(input("Digite o valor a resgistrado » "))
    lst.append(i)
    if i % 2 == 1:
        lst1.append(i)
    else:
        lst2.append(i)

    while True:
        e = str(input("Deseja continuar? [S/N] » ")).strip().upper()[0]
        if e not in "SN":
            print("Opção inválida. Tente novamente!")
        else:
            break
    
    if e == "N":
        break

print(dedent(f"""
                Essa lista contém todos os valores » {lst}\n
                Esssa contém os pares » {lst2}\n
                Essa contém os ímpares » {lst1}\n
            """))