"""
    Exercício Python 084
    Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
    No final, mostre:
        A) Quantas pessoas foram cadastradas.
        B) Uma listagem com as pessoas mais pesadas.
        C) Uma listagem com as pessoas mais leves.
"""
from textwrap import dedent

lst = []
w = []
pmáx = []
pmín = []
cont = 0

while True:
    lst.append([str(input("Name » ")).strip().title(), float(input("Weight » "))])
    w += [lst[cont][1]]
    cont += 1

    while True:
        e = str(input("Do you wish to continue? » ")).strip().upper()[0]
        if e not in "YN":
            print("Invalid option. Try again!")
        else:
            break
    
    if e == "N":
        break

for p in lst:
    if p[1] == max(w):
        pmáx += [p[0]]
    if p[1] == min(w):
        pmín += [p[0]]

print(dedent(f"""
                » '{len(lst)}' people were resgistered.\n
                The biggest weight was '{max(w)}Kg' of {pmáx}\n
                The lowest weight was '{min(w)}Kg of {pmín}
            """))

"""
# Essa é a resolução do Professor Guanabara!

np = []
lst = []
pma = pmi = 0

while True:
    np.append(str(input("Name » ")))
    np.append(float(input("Peso » ")))
    if len(lst) == 0:
        pma = pmi = np[1]
    else:
        if np[1] > pma:
            pma = np[1]
        if np[1] < pmi:
            pmi = np[1]
    lst.append(np[:])
    np.clear()

    while True:
        e = str(input("Deseja continuar? [S/N] » ")).strip().upper()
        if e not in "SN":
            print("Opção inválida. Tente novamente!")
    
        else:
            break
    
    if e == "N":
        break

print(f"\nO total de pessoa(s) cadastrada(s) é {len(lst)}!\nSegue a relação » {lst}")

print(f"\nO maior peso é {pma}. Peso de ", end="")
for p in lst:
    if p[1] == pma:
        print(f"'{p[0]}' ", end="")

print(f"\n\nO menor peso é {pmi}. Peso de ", end="")
for p in lst:
    if p[1] == pmi:
        print(f"'{p[0]}' ", end="")

print()
"""