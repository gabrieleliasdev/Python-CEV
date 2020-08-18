from pattern import title
from textwrap import dedent

title("Lesson '20' content")
print(dedent("""
                » Interactive Help
                » docstrings
                » Argumentos opcionais
                » Escopo de variáveis
                » Retorno de resultados
            """), end='')

title("Interactive Help")
print("See the meaning » help(print) or print(input.__doc__)")

title("docstrings")
print("Function Manual which can be accessed by the command » help(def), example » help(couter)")
def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela.

    Args:
        i (int): início da contagem
        f (int): fim da contagem
        p (int): passo da contagem
        retunr : sem retorno

    """
    c = i
    while c <= f:
        print(f"{c}", end="..")
        c += p
    print("FIM!")
contador(2, 10, 2)
#help(contador)

title("Argumentos Opcionais")
print("Assigning a value of '0' to the arguments makes them optional. The function will work even in the absence of value.")
def somar(a=0, b=0, c=0):
    """
    Faz a soma de três valores e mostra o resultado na tela.

    Args:
        a (int): o  primeiro valor
        b (int): o segundo valor
        c (int): o terceio valor
    """
    s = a + b + c
    print(f"A soma vale {s}")
somar(3, 2)

title("Escopo de Variáveis")
print("Local onde a variável irá existir e local onde a variavel não irá existir.")
def teste(b):
    a = 8
    b += 4
    c = 2
    print(f"A local vale {a}")
    print(f"B local vale {b}")
    print(f"C local vale {c}")
a = 5
teste(a)
print(f"A global vale {a}")

title("Retorno dos Resultados")
def soma(a=0, b=0, c=0):
    s = a + b + c
    return s
r1 = soma(3, 2, 5)
r2 = soma(1, 7)
r3 = soma(4)
print(f"Meus cálculos deram {r1}, {r2} e {r3}.")

title("Practice - Calculate the factorial of a number")
def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

title("Prática - Número Par (True or False)")
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um número: '))
print(par(num))
print('ou')
if par(num):
    print('É par!')
else:
    print('Não é par!')