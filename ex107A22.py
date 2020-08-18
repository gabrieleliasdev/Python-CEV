import pattern
from textwrap import dedent
pattern.title("Modularização")
print(dedent(f"""
                » Surgiu no início da década de 60
                » Sistemas ficando cada vez maiores
                » Foco: dividir um programa grande
                » Foco: aumentar a legibilidade
                » Foco: facilitarn a manutenção\n
                - - - - - - Vantagens - - - - - -\n
                » Organização do código
                » Facilidade na manutenção
                » Ocultação de código detalhado
                » Reutilização em outros projetos
            """))

from lesson22 import numeros
num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'0 fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')