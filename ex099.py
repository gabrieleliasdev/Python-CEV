"""
    Exercício Python #099 - Função que descobre o maior
    Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
    Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from pattern import *
from random import sample
from time import sleep

title("Function that discovers the largest")

def máx(input):     
    if input == 0:
        print("Analyzing past values...")
        print(f"\nTotal amounts reported » {input} | Highest reported value » {input}\n"), line()

    else:
        print("Analyzing past values...")
        r = sample(range(10), input)
        for i in r:
            print(f" » {i}", end='', flush=True)
            sleep(0.5)
        print(f"\nTotal amounts reported » {len(r)} | Highest reported value » {max(r)}"), line()

máx(6), máx(3), máx(2), máx(1), máx(0)

end(), prof()

def maior(* núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados... ')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram inforamdos {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

# Programa principal
maior(2, 9, 4, 5 ,7, 1)
maior(4, 7, 0)
maior(1,2)
maior(6)
maior()