# Empacotamento e desempacotamento de dicionários

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

dados_completo = {**pessoa, **dados_pessoa}

# print(dados_completo)

def show_args(*args, **kwargs):
    print('ARGS:', args)
    print()

    for key, value in kwargs.items():
        print(key, value)

# No caso só nome='Joana' é nomeado
#show_args(1, 2, dados_completo.items(), nome='Joana')

# Mas no caso se eu quiser descerializar
show_args(**dados_completo)
