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
from helper.print_msg_section import print_msg_section

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

# Cria um novo dicionário com o construtor dict
carro = dict(modelo='Corsa', cor='Azul', marca='Chevrolet')

print_msg_section('Create => carro')
print(carro)


# Acessando um valor de um dicionário de maneira simples
nome = pessoa['nome']

print_msg_section('GET => nome')
print(nome)

# Acessa um valor e caso não exista seta um valor default None evitando erros de Exceção
sobrenome = pessoa.get('sobrenomee')

print_msg_section('GET => sobrenome porém caso não exista None será o valor default de sobrenome')
print(sobrenome)


# Atualiza o valor de um item
pessoa['nome'] = 'Vitor'

# Atualiza um objeto e caso os atributos não existam acrescenta os atributos no final do dicionário
pessoa.update({
    'sexo': 'M',
    'cor': 'Branca'
})

print_msg_section('Update => nome')
print(pessoa)


# Remove o item idade e retorna o valor removido
idade = pessoa.pop('idade')

print_msg_section('Delete => idade')
print(pessoa)

# Remove o último item do dicionário é muito similar ao obj.pop() do JavaScript
last_item = pessoa.popitem()

print_msg_section('Delete => endereços')
print(pessoa)
