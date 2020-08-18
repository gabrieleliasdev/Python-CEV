# Escreva  um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule o valor do seu aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%

s = '-=-'*20

m = int(input(f'\n{s}\nReports your salary and the increase will be based on the salary base.\n>>> R$ '))

if m > 1250:
  print('\nYour current salary R$ {:.2f} will increase by 10%.\nFrom now on you will receive: R$ {:.2f}\n{}\n'
        .format(m, m+(m*10/100),s))
else:
  print('\nYour current salary R$ {:.2f} will increase by 15%.\nFrom now on you will receive: R$ {:.2f}\n{}\n'
        .format(m, m+(m*15/100),s))
