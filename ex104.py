"""
    Exercício Python #104 - Validando entrada de dados em Python
    Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input()
    do Python, só que fazendo a validação para aceitar apenas um valor numérico.
    Ex: n = leiaInt('Digite um n: ')
"""
from pattern import title, end, prof
title("Validating data entry in Python"), prof()
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("ERRO! Digite um número inteiro válido.")
        if ok:
            break

        while True:
            res = str(input("Do you wish to continue? [Y/N] » ")).strip().upper()[0]
            if res in "YN":
                break
            print("Option invalid. Try again.")
        
        if res == "N":
            break
    return valor
# Programa Principal
n = leiaInt("Digite um número: ")
print(f"Você abacou de digitar o número {n}"), end()