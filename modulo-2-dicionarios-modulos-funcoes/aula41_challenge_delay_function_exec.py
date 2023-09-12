# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def closure_function(y):
        return funcao(x, y)
    # Retorno a clousure sem executá-la, e seu primeiro parâmetro já estará salvo em memória.
    return closure_function


soma_com_cinco = criar_funcao(soma, 5)(5)
multiplica_por_dez = criar_funcao(multiplica, 10)

result_multipla = multiplica_por_dez(10)

print(f'{soma_com_cinco=}')
