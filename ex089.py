"""
    Exercício Python #089 - Boletim com listas compostas
    Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
    No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
    de cada aluno individualmente.
"""
print(f"{'- = '*16}\n{'School Bulletin with Compound Lists':^64}\n{'- = '*16}")

lst = []
n = 0

while True:
    lst.append([str(input(f"\n({n+1}ª) Registration\nStudents name » ")).strip().title(),
                float(input("First note » ")), float(input("Second note » "))])
    average = (lst[-1][1] + lst[-1][2]) / 2
    lst[-1].insert(3, average)
    n += 1

    while True:
        res = str(input("\nDo you wish to continue? [Y/N] » ")).strip().upper()[0]
        if res not in "YN":
            print("Option invalid. Try again!")
        else:
            break
    
    if res == "N":
        break

print(f"\n{'-=' * 30}\n{'Nª':<4}{'Name':<10}{'Avarege':>8}\n{'-' * 23}")
for c, i in enumerate(lst):
    print(f"{c+1:<4}{i[0]:<10}{i[3]:>8.1f}")

while True:
    a = int(input("\nShow which student's grade? » "))
    if a == len(lst):
        print(f"\nRecord of notes » Student '{lst[a-1][0]}' | First '{lst[a-1][1]}' | Second '{lst[a-1][2]}'")
    elif a != len(lst):
        print("Option invalid. Try again!")

    while True:
        res = str(input("\nDo you wish to continue? [Y/N] » ")).strip().upper()[0]
        if res not in "YN":
            print("Option invalid. Try again!")
        else:
            break
    
    if res == "N":
        print(f"\n{'- = '*16}\n{'End':^64}\n{'- = '*16}")
        break

