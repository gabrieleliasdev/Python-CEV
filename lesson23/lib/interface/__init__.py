
def validate(msg):
    while True:
        try:
            res = int(input(msg))
        except Exception as erro:
            print(f"\033[31mERROR: The problem encountered was » {erro.__class__}, {erro.__cause__}.\033[m")
            continue
        except KeyboardInterrupt:
            print(f"\n\033[31mProgram interrupted by the user.\033[m")
            return 3
        else:
            return res
        
def line(tam = 42):
    return '\033[m-' * tam

def cabeçalho(txt):
    print(line())
    print(txt.center(42))
    print(line())

def menu(lista):
    cabeçalho("MAIN MENU")
    c = 1
    for item in lista:
        print(f"\033[1m{c}\033[m - \033[36m{item}\033[m")
        c += 1
    print(line())
    opc = validate("\033[32mYour Option »\033[m\033[1;32m ")
    return opc
