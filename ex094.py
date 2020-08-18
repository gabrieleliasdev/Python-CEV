"""
    Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
    em um dicionário e todos os dicionários em uma lista. No final, mostre:
        A) Quantas pessoas foram cadastradas
        B) A média de idade
        C) Uma lista com as mulheres
        D) Uma lista de pessoas com idade acima da média
"""
from textwrap import dedent

print(f"{'-=' * 30}\n{'Joining dictionaries and list':^60}\n{'-=' * 30}\n")
dic = {}
lst = []
s = av = 0
w = ab = ""

while True:
    dic["name"] = str(input("Name » ")).strip().title()
    
    while True:
        dic["gender"] = str(input("Gender [M/W] » ")).strip().title()[0]
        if dic["gender"] in "MW":
            break
        print("Option invalid. Try again.")

    dic["age"] = int(input("Age » "))

    s += dic["age"]
    
    if dic["gender"] == "W":
        w += f"'{dic['name']}' "

    lst.append(dic.copy())
    dic.clear()

    while True:
        res = str(input("Do you wish to continue? [Y/N] » ")).strip().upper()[0]
        if res in "YN":
            break
        print("Option invalid. Try again.")
        
    if res == "N":
        break

av = s / len(lst)

for i in lst:
    if i["age"] >= av:
        ab += f"'{i['name']}' "

print(dedent(f"""
                {'-=' * 30}\n
                A) '{len(lst)}' people were registered\n
                B) The average age is » '{av:5.2f}'\n
                C) The registered women were » {w}\n
                D) People above the average age » {ab}
            """))

print(f"\n{'- = '*15}\n{'End':^60}\n{'- = '*15}")

print("\n » Below is the resolution of the Professor Gustavo Guanabara\n")

galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if res in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')