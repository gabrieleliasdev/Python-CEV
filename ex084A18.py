print(f"\n{'Exemple 01':=^40}\n")

dados = ["Pedro",25]
dados1 = ["Maria",19]
pessoas = list()
pessoas.append(dados[:])
pessoas.append(dados1[:])
print(pessoas)
print(len(pessoas))
print(pessoas[0][0])
print(pessoas[1][1])

print(f"\n{'Exemple 02':=^40}\n")

print("O fatimanento '[:]' da lista permite realizar uma cópia da mesma, cortando qualquer vinculo com a 'original.'")

galera = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]}.')

dado = []
totmai = totmen = 0

for c in range(0,3):
    dado.append(str(input("Nome » ")))
    dado.append(int(input("Idade » ")))
    galera.append(dado[:])
    dado.clear()
print(dado)
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        totmai += 1
    else:
        print(f"{p[0]} é menor de idade.")
        totmen += 1

print(f"Temos {totmai} maiores e {totmen} menores de idade.")