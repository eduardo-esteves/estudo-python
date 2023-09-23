
# Aula 191

# O problema aqui é que estamos usando um parâmetro default mutável
# e isso está trazendo um comportamento inesperado de termos sempre
# os mesmos valores em já passada em "lista" desde a sua primeira chamada
def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('Eduardo')
adiciona_clientes('Joana', cliente1)

print(cliente1)

cliente2 = adiciona_clientes('Vitor')
adiciona_clientes('Maria', cliente2)

print(cliente2)
print(cliente1)
