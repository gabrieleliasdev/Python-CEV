"""
    Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
    O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
    que ele conquistou no final do jogo.
"""
from random import randint

v = 0

while True:
    bot = randint(0, 11)
    
    user = int(input("Type a number » "))
    
    sm = bot + user
    
    res = ' '
    
    while res not in 'EO':
        res = str(input("Even or Odd? [E/O] » ")).strip().upper()
    
    print(f"Bot chose: {bot} | Your chose: {user} | Total {sm}")       
    
    if res == 'E':
        if sm % 2 == 0:
            print("You won!")
            v += 1
        else:
            print("You lost.")
            break
    
    elif res == "O":
        if sm % 2 == 1:
            print("You won!")
            v += 1
        else:
            print("You lost")
            break
    
    print("Let's play again...")

print(f"Game Over! You won {v} times, congratulations!!")