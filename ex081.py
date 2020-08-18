""" 
    Exercício Python #081 - Extraindo dados de uma Lista
    Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
        A) Quantos números foram digitados.
        B) A lista de valores, ordenada de forma decrescente.
        C) Se o valor 5 foi digitado e está ou não na lista.
"""

lst = []

while True:
    i = int(input("Digite um número » "))
    lst.append(i)
    
    while True:
        e = str(input("Deseja continuar? [S/N] » ")).strip().upper()[0]
        if e not in "SN":
            print("Erro: Opção inválida. » Tente novamente.")
        else:
            break
    if e == "N":
        break
print('-='*30)
print(f"Foram registrados '{len(lst)}' » {lst}")

print(f"Este são os valores em ordem decrescente » {sorted(lst, reverse=True)} by:sorted")

lst.sort(reverse=True)
print(f"Este são os valores em ordem decrescente » {lst} by:sort")

if 5 in lst:
    print("O valor '5' faz porte da lista!")
else:
    print("O valor '5' não faz parte da lista.")