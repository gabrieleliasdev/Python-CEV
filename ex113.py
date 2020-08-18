"""
   Exercício Python #113 - Funções aprofundadas em Python
   Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""
from pattern import title, end
from lesson22 import validate

title("In-depth Python Functions")

i = validate.integer("Type a integer number » ")
r = validate.real("Type a real number » ")
print(f"The integer reported was {i} and the real was {r}")

end()
