"""
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
lst = []

n = sm = cont = s = 0

while s != "N":
    n = int(input("Type values you want to be added » "))
    sm += n
    cont += 1
    lst += [n]
    s = str(input("Do you wish to continue? [Y/N] » ")).strip().upper()

print("Data » Typed value: {}\n"
      "Amount of values: {} | Sum of values {} | Average values: {} | Value max: {} | Value Min: {}"
      .format(lst, cont, sm, sm/cont, max(lst), min(lst)))
