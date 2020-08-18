"""
    Exercício Python #090 - Dicionário em Python
    Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
    No final, mostre o conteúdo da estrutura na tela.
"""
print(f"{'- = '*16}\n{'Dictionary':^64}\n{'- = '*16}")

dic = {}
lst = []

while True:
    dic = {
            "Student": str(input("\nName of the Student » ")).strip().title(),
            "Average": float(input("Student average » ")),
          }

    if dic["Average"] >= 6:
        dic["Situation"] = "Approved"
    elif 5 <= dic["Average"] < 6:
        dic["Situation"] = "Recuperation"
    else:
        dic["Situation"] = "Reproved"
    
    lst.append(dic.copy())

    while True:
        res = str(input("\nDo you wish to continue? [Y/N] » ")).strip().upper()[0]
        if res not in "YN":
            print("Option invalid. Try again.")
        else:
            break
    
    if res == "N":
        break

print("\nBelow is the student data:")
for s in lst:
    print()
    for k, v in s.items():
        print(f" - {k} » {v}")

print(f"\n{'- = '*16}\n{'End':^64}\n{'- = '*16}")

print("\n » Below is the resolution of the Professor Gustavo Guanabara\n")

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovação'
print('-=' * 30)
for k, v in aluno.items():
    print(f"{k} é igual a {v}")
