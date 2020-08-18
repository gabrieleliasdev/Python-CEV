def money(msg):
    valid = False
    while not valid:
        enter = str(input(msg)).replace(',', '.').strip()
        if enter.isalpha() or enter == '':
            print(f"\033[0;31mERROR: '{enter}' is {type(enter)}. Typing a value valid!\033[m")
        else:
            valid = True
            return float(enter)

def integer(msg):
    while True:
        try:
            enter = int(input(msg))
        except Exception as erro:
            print(f"\033[31mERROR: The problem encountered was » {erro.__class__}, {erro.__cause__}.\033[m")
            continue
        except KeyboardInterrupt:
            print(f"\n\033[31mProgram interrupted by the user.\033[m")
            return 0
        else:
            return enter

def real(msg):
    while True:
        try:
            enter = float(input(msg))
        except Exception as erro:
            print(f"\033[31mERROR: The problem encountered was » {erro.__class__}, {erro.__cause__}.\033[m")
            continue
        except KeyboardInterrupt:
            print(f"\n\033[31mProgram interrupted by the user.\033[m")
            return 0
        else:
            return enter