"""
    Exercício Python #100 - Funções para sortear e somar
    Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
    A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
    mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""
from pattern import title, end, prof
from random import sample, randint
from time import sleep

title('Functions for Raffle and Sum')

lst = []

def raffle(input):       
    r = sample(range(10), input)
    print(f"Sorting {len(r)} values from the list » ", end='')
    for i in r:
        lst.append(i)
        print(i, end=' ', flush=True), sleep(0.5)

def sm():
    s = []
    for i in lst:
        if i % 2 == 0:
            s += [i]
    print(f"\n\nEven values are {s} and their sum is » {sum(s)}"), sleep(1)

raffle(5), sm(), end(), prof()
 
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

números = list()
sorteia(números)
somaPar(números)