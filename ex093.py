"""
   Exercício Python #093 - Cadastro de Jogador de Futebol
   Crie um programa que gerencie o aproveitamento de um jogador de futebol.
   O programa vai ler o nome do jogador e quantas partidas ele jogou.
   Depois vai ler a quantidade de gols feitos em cada partida.
   No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
print(f"{'-=' * 30}\n{'Football Player Registration':^64}\n{'-=' * 30}")

dic = {
        "Footballer": str(input("Player's name » ")).strip().title(),
        "Soccer Matches": int(input("How many games have you played? » "))
      }

lst = []
n = 0

for i in range(dic["Soccer Matches"]):
     lst.append(int(input(f"How many goals in the {n+1}ª matches? » ")))
     n += 1

dic["Gols History"] = lst
dic["Football Performance"] = sum(lst)

print('=' * 60)
print(dic)

print('=' * 60)
for k, v in dic.items():
    print(f"{k} » {v}")

print('=' * 60)
print(f"The player '{dic['Footballer']}', played '{dic['Soccer Matches']}' matches.")
for pos, i in enumerate(lst):
    print(f"   » At the match {pos+1}ª, scored {i} goals.")
print(f"\n   » Total of {dic['Football Performance']} gols!")

print(f"\n{'- = '*15}\n{'End':^64}\n{'- = '*15}")

print("\n » Below is the resolution of the Professor Gustavo Guanabara\n")

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'      =>Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')