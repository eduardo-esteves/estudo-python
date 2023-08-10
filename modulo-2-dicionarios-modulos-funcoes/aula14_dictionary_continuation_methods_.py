# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

from copy import copy, deepcopy

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

# Acessar atributos com get() evita "Key Error" além de podemos setar
# um valor padrão passando um segundo parametro, em caso de não existir a key.
pessoa.get('cor')

# pop() Além de apagar a key, retorna o valor apagado
nome = pessoa.pop('nome')

print(f'{nome=} \n {pessoa}')

# popitem() remove o último item do dicionario e retorna sua key e valor em tupla
last_key = pessoa.popitem()

print(pessoa)

pessoa.update({
    'nome': 'Eduardo',
    'sobrenome': 'Silva'
})

print()
print('111111111111111111111111111')
print(pessoa)

pessoa.update(nome='Eduardo Esteves', sobrenome='Esteves')

print()
print('22222222222222222222222222222')
print(pessoa)

# No update ainda podemos passar uma tupla() para atualizar seus valores
# é importante notar em caso de declararmos apenas um valor não podemos
# esquecer de declarar a virgula após esse valor

tupla = (('nome', 'Vitor Esteves'),)
pessoa.update(tupla)

print()
print('3333333333333333333333333333')
print(pessoa)
