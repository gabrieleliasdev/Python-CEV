"""
    Exercício Python #092 - Cadastro de Trabalhador em Python
    Crie um programa que leia nome, ano de nascimento e carteira de trabalho
    e cadastre-o (com idade) em um dicionário.
    Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
    Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date, datetime

print(f"{'- = '*16}\n{'Worker Registration':^64}\n{'- = '*16}")

dic = {}

while True:
    dic["Worker"] = str(input(f"Name of the Worker » ")).strip().title()
    birth = int(input("Year of birth » "))
    dic["Age"] = date.today().year - birth
    dic["CTPS"] = int(input("CTPS Nª ('0', if you have not) » "))

    if dic["CTPS"] != 0:
        dic["Hiring"] = int(input("Year of hiring » "))
        dic["Salary"] = float(input("Salary » R$ "))
        dic["Retirement"] = dic["Age"] + ((dic["Hiring"] + 35) - datetime.today().year)

    while True:
        res = str(input("\nDo you wish to continue? [Y/N] » ")).strip().upper()[0]
        if res not in "YN":
            print("Option invalid. Try again.")
        else:
            break

    if res == "N":
        break

print()
for k, v in dic.items():
    print(f"{k} » {v}")

print(f"\n{'- = '*16}\n{'End':^64}\n{'- = '*16}")

print("\n » Below is the resolution of the Professor Gustavo Guanabara\n")

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de TRabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')