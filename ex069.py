"""
    Crie um programa que leia a idade e o sexo de várias pessoas.
    A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
    No final, mostre:
    A) quantas pessoas tem mais de 18 anos.
    B) quantos homens foram cadastrados.
    C) quantas mulheres tem menos de 20 anos.
"""
lst = []
a_cont = m_cont = af_cont = 0
art_a = 'Registration of people'
while True:
    print('- = '*16)
    print(f"{art_a:^64}")
    print('- = '*16)
    n = str(input("Inform the name of the person you wish to register » ")).strip().title()
    a = int(input("Inform age » "))
    g = ' '
    while g not in 'MF':
        g = str(input("Inform gender [M/F] » ")).strip().upper()[0]
    print('- -'*10)
    
    lst += [n, a, g]
   
    if a >= 18:
        a_cont += 1
   
    if g == "M":
        m_cont += 1
    
    if g == "F" and a < 20:
        af_cont += 1
    
    r = ' '
    while r not in 'YN':
        r = str(input("Do you want to register again? [Y/N] » ")).strip().upper()[0]
    if r != 'Y':
        print(f"\n» {a_cont} people are over 18 | » {m_cont} men were registered | » {af_cont} women are under 20\n")
        break
    
print(lst)
