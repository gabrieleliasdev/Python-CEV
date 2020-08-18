"""039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
  - Se ele ainda vai se alistar ao serviço militar.
  - Se é a hora de se alistar.
  - Se já passou do tempo do alistamento
  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date

dy = date.today().day
my = date.today().month
yy = date.today().year

today = [dy, my, yy,]

#db = int(input(f"Date of birth:{int(input('Day: '))}/{int(input('Month: '))}/{input('Year: ')}"))

da = int(input("Day: "))
ma = int(input("Month: "))
ya = int(input("Year: "))

print('Your date of birth: {}/{}/{}. You are {} years old.'.format(da,ma,ya,ya))

print(f'{(dy-da)}/{my-ma}/{yy-ya}')

birth = [da, ma, ya]

dataNasc = datetime.date(da,ma,ya)
dataAtual = datetime.date(dy,my,yy)

diferença = (dataAtual - dataNasc)

result = (diferença.days / 365.25)

print(f'{result}')

