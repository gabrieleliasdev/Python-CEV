""" 072
    Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
    Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
print("\n{:=^50}\n".format("Exercise 72"))

lst = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
       "twelve", "thirteen", "cartoze", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty")


while True:
    n = int(input("Type a number betwenn 0 and 20 » "))
    if 0 <= n <= 20:
        break
    print("Try again.")

print(f"You typed » {lst[n]}")