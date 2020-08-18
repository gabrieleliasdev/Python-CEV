def ex(input):
    print(f"\n{' Exemple {} ':=^30}\n".format(input))
ex(1)
def mensagem(msg):
    print('-' * 30)
    print(f"{msg:^30}")
    print('-' * 30)
mensagem("Teste")
ex(2)
def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)
título(f"{'CURSO EM VÍDEO':^30}")
título(f"{'PYTHON É UMA DELÍCIA!':^30}")
título(f"{'GABRIEL ELIAS':^30}")
ex(3)
def soma(a, b):
    s = a + b
    print(s)

soma(4, 5)
soma(8, 9)
soma(2, 1)
ex(4)
def som(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}\n')

som(4, 5)
som(b=4, a=5)
ex(5)
def contador(* núm):
    tam = len(núm)
    print(f"Recebi os valores {núm} e são ao todo {tam} números.")
    for valor in núm:
        print(f"{valor} ", end="")
    print("FIM!\n")

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
ex(6)
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
ex(7)
def sm(* valores):
    s = 0
    for num in valores:
        s += num
    print(f"Somando os valores {valores} temos {s}")
sm(5, 2)
sm(2, 9, 4)
