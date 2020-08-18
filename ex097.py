"""
    Exercício Python #097 - Um print especial
    Faça um programa que tenha uma função chamada área(),
    que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""
from pattern import *

title("A special Print")
prof()

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

escreva('Gabriel Elias')
escreva('Curso de Python no Youtube')
escreva('CeV')

end()
