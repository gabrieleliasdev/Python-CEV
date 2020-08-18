# Manipulando Texto

pharse = 'I can do all things through Christ, who strengthens me.'

print(f'\n{pharse}\n')

print(f'Inform only this character "[7]": {pharse [7]}\n')

print(f'Reports the characters from 0 to 7 "[0:8]": {pharse [0:8]}\n')

print(f'Reports the characters from 8 to the last "[8:]": {pharse [8:]}\n')

print(f'Reports the characters from the frist to the last by jumpping 2 by 2 "[::2]": {pharse [::2]}\n')

print(f'Reports length "len()": {len(pharse)}\n')

print(f'Counts the number of times the character appears "count("h")": {pharse.count("h")}\n')

print(f'Counts the number of times the character appears from 0 to 25 "count("h",0,25)": {pharse.count("h",0,25)}\n')

print(f'Informs when "its" started |find("ist")|: {pharse.find("ist")}\n')

print(f'Reports with True or False if this character exists |"Christ" in|: {"Christ" in pharse}\n')

print(f'Will reposition, replace, one character whth another "replace("Y","X")": {pharse.replace("Christ","Jesus")}\n')

print(f'All characters will be capitalized "upper()": {pharse.upper()}\n')

print(f'All characters will be in lower case "lower()": {pharse.lower()}\n')

print(f'Only the frist character will be in upper case, the others will be in lower case "capitalized()": {pharse.capitalize()}\n')

print(f'The first charater of each word will be capitalized "title()": {pharse.title()}\n')

print(f'Remove excess spaces from the string "strip() or rstrip, lstrip": {pharse.strip()}\n')

print(f'Creats a new list where it make each character a string based on the spacing between them "split()": {pharse.split()}\n')

print(f'Junction - is the inverse of split. It will separate strings together |"-".join()| {"-".join(pharse)}\n')


