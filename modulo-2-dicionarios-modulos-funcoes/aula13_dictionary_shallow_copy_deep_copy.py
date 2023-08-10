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

# Isso não faz uma cópia do objeto pessoa, e sim pessoa2 vai apontar para o
# mesmo endereço em mémoria de pessoa, ou seja caso alteremos uma key de
# pessoa, isso vai refletir no objeto pessoa2
pessoa2 = pessoa

# Altero seu valor
pessoa2['nome'] = 'João'

# A alteração acima vai refletir no objeto pessoa devido ambos estarem
# apontado para o mesmo endereço em memória
print(pessoa['nome'])
print()

# Com copy() faz uma "shallow copy" e não ocorre atribuição por referência e
# sim de valores, porém é bom lembrar que essa é uma cópia rasa por atribuição
# e não faz a copia em keys de Objetos mais complexos que possuem subniveis,
# exemplo, endereço.
pessoa3 = pessoa2.copy()

# Fazendo uso de copy do modulo copy
pessoa4 = copy(pessoa2)

# Com o uso de deepcopy os valores da copia será imutavel porém demanda muito processamento e memoria
pessoa5 = deepcopy(pessoa2)

# Em caso de alteração de pessoa2 isso não vai refletir em pessoa3
pessoa2['nome'] = 'Eduardo Esteves'
pessoa2['endereços'][0]['rua'] = 'Para ter o comportamento de imutavel deve ser feito com copy.deepcopy()'

print(pessoa3)
print()

print(pessoa4)
