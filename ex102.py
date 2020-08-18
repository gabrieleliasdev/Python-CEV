"""
    Exercício Python #102 - Função para Fatorial
    Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre
    Interactive Help em Python, o uso de docstrings para documentar nossas funções, argumentos opcionais
    para dar mais dinamismo em funções Python, escopo de variáveis e retorno de resultados.
"""
from pattern import title, end, prof
title("Function for Factorial")
def fact(i=0, s=0, h=0):
    """This function calculates the factorial of a number

    Args:
        i (int): Input of the number to be factored
        s (str): If selected "Y", will show the calculation
        h (str): If selected "Y", will show the docstrings of function

    Returns:
        print: Shows the factorial of the number entered (i)
    """
    f = 1
    for c in range(i, 0, -1):
        if s == "Y":
            print(f"{c}", end=" ")
            if c > 1:
                print(f"x", end=" ")
        f *= c 
 
    if s == "Y":
        print(f"» {f}")
    
    if h == "Y":
        return help(fact)
    
    return f"The factorial of {i} is '{f}'"
        
i = int(input("Type the number to know your factorial » "))
s = str(input("Do you whant to see the calculation? [Y/N] » ")).strip().upper()[0]
h = str(input("Do you what to see the docstrings for this function? [Y/N] » ")).strip().upper()[0]
print(fact(i, s, h))

end(), prof()
def fatorial(n, show=True):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

#Programa Princial
print(fatorial(5, show=True))

print(fatorial(5))