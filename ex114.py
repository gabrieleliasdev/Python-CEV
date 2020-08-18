import urllib
import urllib.request

try:
    website = str(input("Type a werbsite » "))
    site = urllib.request.urlopen(f"http://{website}")
except:
    print(f"The \033[4;1;3;31m{website}\033[m website is currently not acessible!")
else:
    print(f"The \033[4;1;3;32m{website}\033[m website is currently accessible!")
