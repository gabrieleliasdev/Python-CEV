"""
   Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
   um dicionário com as seguintes informações:
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação (opcional)

    Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
"""
from pattern import title
title("Analyzing and Generating Dictionaries")

def notes(msg):
    note = 0
    lst = []
    dic = {}
    while True:
        i = float(input(msg))
        if i == float(i):
            note = float(i)
            lst += [note]
        else:
            print(f"Invalid data. Please enter a number.")
        
        while True:
            res = str(input("Do you wish to continue? [Y/N] » ")).strip().upper()[0]
            if res in "YN":
                break
            print("Option invalid. Try again.")
            
        if res == "N":
            break

        dic = {
                "Total Notes": len(lst),
                "Highest grade": max(lst),
                "Lowest grade": min(lst),
                "Class Average": sum(lst) / len(lst)
              }
        if dic["Class Average"] < 5:
            dic["Situatin"] = "Bad"
        elif dic["Class Average"] < 7:
            dic["Situatin"] = "Reasonable"
        else:
            dic["Situatin"] = "Good"
        
    return dic

i = notes(f"Enter the note » ")
print(i)

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :paran sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

#Programa Principal
resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)
help(notas)