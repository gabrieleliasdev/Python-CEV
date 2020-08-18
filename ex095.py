"""
    Exercício Python #095 - Aprimorando os Dicionários
    Aprimore o desafio 93 para que ele funcione com vários jogadores,
    incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
print(f"{'-=' * 30}\n{'Improving Dictionary':^64}\n{'-=' * 30}")

lst_dic = []

while True:
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

    lst_dic.append(dic.copy())
    dic.clear()

    while True:
        res = str(input("Do you wish  to continue? [Y/N] » ")).strip().upper()[0]
        if res in "YN":
            break
        print("Option invalid. Try again.")

    if res == "N":
        break

print('=' * 60)
print(f"     {'Cod':^5}   {'Player':^12}   {'Gols History':^16}   {'Total Gols':^12}")
for pos, i in enumerate(lst_dic):
    print(f"   » {(pos+1):^5} | {i['Footballer']:^12} |"
          f" {str(i['Gols History']):^16} | {i['Football Performance']:^12}")

print('=' * 60)
while True:
    e = int(input("\nWant you show the performance of what players? ['0' to finish] » "))
    if e == 0:
        break

    if len(lst_dic) < e > len(lst_dic):
        print("Option invalid. Try again.")

    else:
        for k, v in lst_dic[e-1].items():
            print(f"{k} » {v}")

        print(f"\n» or\n")

        print(f"The player '{lst_dic[e-1]['Footballer']}', played '{lst_dic[e-1]['Soccer Matches']}' matches.")
        for pos, i in enumerate(lst_dic[e-1]['Gols History']):
            print(f"   » At the match {pos+1}ª, scored {i} goals.")

print(f"\n{'- = '*15}\n{'End':^64}\n{'- = '*15}")

print("\n » Below is the resolution of the Professor Gustavo Guanabara\n")

time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if res in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == "N":
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
        print('-' * 40)
    print('<< VOLTE SEMPRE >>')
    