"""
    Exercício Python #088 - Palpites para a Mega Sena
    Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
    O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
    cadastrando tudo em uma lista composta.
"""
from random import sample
from time import sleep

print(f"{'- = '*16}\n{'Guesses for Mega Sena':^64}\n{'- = '*16}")

lst = []
n = 0

res = int(input("\nHow many games do you want to be generate? » "))

print(f"\nSorting '{res}' Games\n")

for i in range(res):
    draw = sample(range(60), 6)
    if draw not in lst:
        lst.append(draw)
    
    print(f"{n+1}ª Bet » {sorted(draw)}")
    n += 1
    sleep(1)

print(f"\n{'- = '*16}\n{'Good Luck!':^64}\n{'- = '*16}")

print("\n » Below is the resolution of the Professor Gustavo Guanabara\n")

from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 40)
print('            JOGA NA MESA SENA            ')
print('-' * 40)
quant = int(input("Quantos jogos você quer que eu sorteie? "))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f"Jogo {i+1}: {l}")
    sleep(1)
print("-=" * 5, "< BOA SORTE! >", "-=" * 5)