"""
    Exercício Python #101 - Funções para votação
    Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
    o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
    OPCIONAL e OBRIGATÓRIO nas eleições.
"""
from pattern import title, end, prof
from datetime import date

title("Voting Functions")
def vote(i):
    v = date.today().year - i
    if v < 16:
        return f"\nWith {v} years » Cannot vote."
    elif v < 18 or v > 65:
        return f"\nWith {v} years » Optional vote."
    else:
        return f"\nWith {v} years » Mandatory vote."

i = int(input("Type date of birth » "))

print(vote(i)), end(), prof()

def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

nasc = int(input("Em que ano você nasceu? "))

print(voto(nasc))