"""
Um dicionário em Python é uma coleção não ordenada de itens. Cada item do dicionário
é uma chave-valor, onde a chave é única e é usada para acessar seu valor correspondente.
Os dicionários são mutáveis, o que significa que você pode adicionar, modificar ou remover
itens após a criação do dicionário.

- Chaves Únicas: As chaves em um dicionário devem ser únicas. Se você tentar adicionar
uma chave que já existe, ela substituirá o valor existente associado a essa chave.

- Mutabilidade: Dicionários são mutáveis, o que significa que você pode adicionar,
modificar ou remover itens.

- Tipos de Dados nas Chaves e Valores: As chaves podem ser de qualquer tipo imutável
(como strings, números ou tuplas). Os valores podem ser de qualquer tipo de dado.

- Métodos e Operações: Os dicionários em Python oferecem vários métodos e operações que
facilitam a manipulação dos dados, como adição de itens, remoção de itens, verificação
de existência de uma chave, iteração sobre itens, etc.
"""

from helper.iterable import is_iterable, has_attr


pessoa = {
    'nome': 'Eduardo Esteves',
    'sobrenome': 'Esteves',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}

print('quantidade de itens => ', pessoa.__len__())

if is_iterable(pessoa) or has_attr(pessoa, '__iter__'):
    for key, value in pessoa.items():
        print(key, '=> ', value)
