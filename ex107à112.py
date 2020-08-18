from pattern import title, end
from textwrap import dedent
from lesson22 import coin, validate
title("Exercising Python Modules")
title('ex107 + ex108 + ex109 + ex110 + ex111 + ex112')
p = validate.money("Enter price » R$ ")

print(dedent(f"""
                 The half of {coin.money(p)} is » {coin.half(p, True)}\n
                 The double of '{coin.money(p)}' is » {coin.double(p, True)}\n
                 Increasing '10%', we have » {coin.increase(p, 10, True)}\n
                 Reducing '13%', we have » {coin.decrease(p, 13, True)}
            """))
title("Resume")
coin.resume(p, 80, 35)

end()
"""
     Exercício Python #107 - Exercitando módulos em Python
     Crie um módulo chamado moeda.py que tenha as funções incorporadas
     aumentar(), diminuir(), dobro() e metade().
     Faça também um programa que importe esse módulo e use algumas dessas funções.
     -
     Exercício Python #108 - Formatando Moedas em Python
     Adapte o código do desafio #107, criando uma função adicional chamada moeda()
     que consiga mostrar os números como um valor monetário formatado.
     -
     Exercício Python #109 - Formatando Moedas em Python
     Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
     informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
     desenvolvida no desafio 108.
     -
     Exercício Python #111 - Transformando módulos em pacotes
     Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
     Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e
     mantenha tudo funcionando.
     -
     Exercício Python #112 - Entrada de dados monetários
     Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
     Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
     mas com uma validação de dados para aceitar apenas valores que seja monetários.
"""