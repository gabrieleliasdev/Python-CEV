from lesson22.validate import integer
from lesson23.lib.interface import *
from lesson23.lib.archive import *
from textwrap import dedent

arq = 'cursoemvideo.txt'

if not archiveExist(arq):
    creatArchive(arq)

while True:
    res = menu(['Ver pessoas cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if res == 1:
        # Opção de listar o conteúdo de um arquivo!
        readArchive(arq)
    elif res == 2:
        # Opção de cadastrar uma nova pessoa.        
        cabeçalho('Novo Cadastro')
        name = str(input('Name: '))
        age = integer('Age: ')
        cadastrar(arq, name, age)
    elif res == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')

'''
while True:
    res = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do Sistema"])
    if res in (1,2,3):
        print(dedent(f"""\
                         \033[m{line()}
                         {'Option {}'.center(42).format(res)}
                         {line()}
                         Finished System
                    """))
        break
    else:
        print("\n\033[31mThis option is not valid.\033[m")
'''
