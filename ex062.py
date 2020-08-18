"""
    062 - Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
    encerra quando ele disser que quer mostrar 0 termos.
"""

ft = int(input("Type the first term: "))
r = int(input("Ratio: "))

term = ft
cont = 1
total = 0
more = 10

while more != 0:
    total = total + more
    while cont <= total:
        print("{} → ".format(term), end="")
        term += r
        cont += 1
    print("break")
    more = int(input("Inform how many more terms, you want to be shown?\n>>> "))

print(f"Total terms presentend {total}")

print("End")