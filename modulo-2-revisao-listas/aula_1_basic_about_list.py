from helper.print_msg_section import print_msg_section


# PCP 31
pessoas = ['Vitor', 'Danny', 'Larissa', 'Patricia', 'João', 'Maria', 'Eduardo']

# Apenas retorna o último elemento da lista sem remove-lo
eduardo = pessoas[-1]
# Remove e retorna o último elemento da lista removido
eduardo_ = pessoas.pop()

print(eduardo_)
print_msg_section('Removeu o último elemento "Eduardo" da lista')
print(pessoas)

# Também é possível acessar um intervalo da lista neste exemplo
# de Danny a João, isso porque o último elemento é sempre
# excluido quando acessamos via intervalos, isso tanto para indices
# positivos quanto negativos.
nomes = pessoas[1:-1]
print_msg_section('Imprime de Danny ao penúltimo elemento João')
print(nomes)

# Em casos de querer acessar do penúltimo elemento ao último
# através de intervalos podemos simplesmente omitir o último elemento
dois_ultimos = pessoas[-2:]
print_msg_section('Imprime a partir do penultimo elemento')
print(dois_ultimos)

