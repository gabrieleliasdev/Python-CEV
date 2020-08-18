from lesson23.lib.interface import cabeçalho

def archiveExist(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def creatArchive(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('There was an ERROR in creating the file.')
    else:
        print(f'{name} file created successfully!')

def readArchive(name):
    try:
        a = open(name, 'rt')
    except:
        print('ERRO in read the archive!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        # print(a.read())
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, name='Desconhecido', age=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print('There was an ERROR na hora de escrever os dados!')
        else:
            print(f'Novo registro de {name} adicionado.')
            a.close()