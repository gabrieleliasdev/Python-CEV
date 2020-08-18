"""
    Exercício Python #091 - Jogo de Dados em Python
    Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
    Guarde esses resultados em um dicionário em Python.
    No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter

print(f"{'- = '*16}\n{'Dice Games':^64}\n{'- = '*16}")

dic = {}

for i in range(0, 4):
    bot = randint(1, 6)
    dic[f"Player({i+1})"] = bot

print("Values rolled on the die:")
for k, v in dic.items():
    print(f"The {k} rolled {v} on the die.")
    sleep(1)

print("\nBelow is the Ranking:")
lst = sorted(dic.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(lst):
    print(f"{i+1}ª Place » {v[0]} with {v[1]} Pts.")
    sleep(1)

print(f"\n{'- = '*16}\n{'End':^64}\n{'- = '*16}")

print("\n » Below is the resolution of the Professor Gustavo Guanabara\n")

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

ranking = list()

print("Valores sorteados:")
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f"  {i+1}ª lugar: {v[0]} com {v[1]}.")
    sleep(1)