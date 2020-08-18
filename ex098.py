"""
    Exercício Python #098 - Função de Contador
    Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
    Seu programa tem que realizar três contagens através da função criada:
    a) de 1 até 10, de 1 em 1
    b) de 10 até 0, de 2 em 2
    c) uma contagem personalizada
"""
from ex089 import i
from pattern import *
from time import sleep

title('Counter Function')

def counter(a, b, c):
    if c < 0:   
        c = -c
    print(f"Count from {a} to {b} of {c} in {c}")
    sleep(2)

    if c == 0:
        c = 1
    if b > a:
        if b >= 0:
            b += 1
    if a > b:
        b -= 1
        c = -c
  
    for i in range(a, b, c):
        print(i, end=' ', flush=True)
    sleep(0.5)   

counter(1, 10, 1)
print("\n")
counter(10, 0, 2)
print("\n\nNow it's your turn to customize your count")
counter(
        a = int(input("Start » ")),
        b = int(input("End » ")),
        c = int(input("Step » "))
        )

end()
prof()

def contador(i, f, p):
    if p < 0:
        p += -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')

# Programa princial
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)