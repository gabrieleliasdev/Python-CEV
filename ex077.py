""" 077
    Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
    Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
lst = "Amor", "Paixao", "Vida", "Solidariedade", "Cristo"

for p in lst:
    print(f"\nNa palabra '{p}', temos as vogais:", end=" ")
    for l in p:
        if l.lower() in "aeiou":
            print(f"{l}", end=" ")
print("\n\nFim\n")