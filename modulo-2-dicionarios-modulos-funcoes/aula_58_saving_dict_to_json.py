import json

# Aula 190
pessoa = {
    'nome': 'Eduardo',
    'sobrenome': 'Esteves',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None
}

file_name = 'aula_58_dict_to_json.json'

# Caso o arquivo ainda não exista, será criado, caso já exista será sobreescrito.
with open(file_name, 'w', encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo)

# Faço a leitura do arquivo criado e carrego seus dados para a estrutura dict do Python.
with open(file_name, 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
