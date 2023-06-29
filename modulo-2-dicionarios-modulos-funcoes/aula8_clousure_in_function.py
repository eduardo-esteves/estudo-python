"""
Closure e funções que retornam outras funções
"""

def print_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


bom_dia = print_saudacao('Bom dia')
boa_noite = print_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(bom_dia(nome))
    print(boa_noite(nome))
