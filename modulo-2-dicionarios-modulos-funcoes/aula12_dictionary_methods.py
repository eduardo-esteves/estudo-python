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

lenght = pessoa.__len__()
lenght2 = len(pessoa)

# O resultado das funções são identicas
print(f'{lenght=} {lenght2=}')

# Atribuindo um objeto do tipo dict_keys, também podemos fazer a conversão para list(all_keys)
all_keys = pessoa.keys()

print()
print(all_keys, type(all_keys))

# Aqui faço a conversão para que eu possa manipular o objeto tupla
new_tuple = tuple(all_keys)

print()
print(new_tuple, type(new_tuple))
print()

# Retorna um dict_items com seus indices e valores, útil para fazer um enumarate
print(pessoa.items())
print()

for chave, valor in pessoa.items():
    print(chave, valor)

# Muito útil para setar um novo valor por padrão caso a key não exista
pessoa.setdefault('idade', 0)

print(f'{pessoa["idade"]=}')
