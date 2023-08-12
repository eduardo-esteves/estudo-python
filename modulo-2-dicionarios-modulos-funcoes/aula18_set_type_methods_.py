# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard


s1 = set()
s1.add('Luiz')

print(s1)

# No update caso queremos passar uma string literal diretamente no construtor, essa
# deverá ser uma tupla, para não termos seus caracteres segmentados devido set ser interavel.
s1.update(('Olá Mundo!',))
print()

print(s1)

# Limpa todos os valores dentro de um set
# s1.clear()

# Já no caso de deletar um valor, sabemos que set não trabalha com indices e
# sim somente valores imutáveis, então não vamos ter erros em descartar valores
# especificos com receio desse valor ter sido alterado no ponto do discard()
s1.discard('Olá Mundo!')
print()

print(s1)

