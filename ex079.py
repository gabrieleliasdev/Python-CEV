""" 079
    Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
    Caso o número já exista lá dentro, ele não será adicionado.
    No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
lst = []
print("Cadastro de valores númericos")
while True:
    i = int(input("\nDigite um valor a ser cadastrado: "))
    if i not in lst:
        lst.append(i)
        print("Valor adicionado com sucesso...")
    else:
        print("Valores duplicados não serão adicionados. Tente novamente.")

    while True:
        e = input("\nQuer continuar? [S/N] ").strip().upper()[0]
        if e not in "SN":
            print("Escolha uma opção válida. Tente novamente.")
        else:
            break
    
    if e == "N":
        break


lst.sort(), print(), print("=-" * 35)
print(f'Este foram os valores cadastrados em ordem crescente: {str(lst).replace("[", "").replace("]", "")}.')
print("=-" * 35)
