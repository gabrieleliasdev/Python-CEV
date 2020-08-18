"""
    Exercício Python #103 - Ficha do Jogador
    Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
    o nome de um jogador e quantos gols ele marcou.
    O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado.
"""
from pattern import title, end, prof

title("Player record")
def record(n='', g=''):
    if n == '':
        n = '<unknown>'
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    
    return f"Player '{n}' has scored {g} goal(s) in the league."

n = str(input("Type a name » ")).strip().title()
g = input("Number of goals  » ")

print(record(n, g))

end(), prof()
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

#Programa Principal
n = str(input("Nome do Jogador: "))
g = str(input("Número de Gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
