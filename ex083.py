"""
    Exercício Python #083 - Validando expressões matemáticas
    Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
    Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
    e fechados na ordem correta.
"""

i = str(input("\nDigite a expressão que deseja ser validada » ")).strip()
if i.count("(") != i.count(")"):
    print("\nHá divergência na quantidade de parênteses.\n")

p1 = "("
p2 = ")"

if i[0] != p1:
    print(f"Há um erro no ínicio da expressão » {i[0]}")
if i[-1] != p2:
    print(f"Há um erro no final da expressão » {i[-1]}")
