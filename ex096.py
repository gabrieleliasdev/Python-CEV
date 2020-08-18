"""
    Exercício Python #096 - Função que calcula área
    Faça um programa que tenha uma função chamada área(),
    que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""
from pattern import *
title("Land Control")

def area():
    print(f"The land area {w}x{l} is {w*l}m²")

w = float(input('WIDTH (m) » '))
l = float(input('LENGTH (m » '))
area()

end()
prof()

def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')

print(' Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
