x = ("Gabriel", "Danny", "Arthur", "Danny")
# Atribuindo cada valor da tupla em uma variável
(nome_1, nome_2, nome_3, nome_4) = x

print(f'{nome_1=}, {nome_2=}, {nome_3=}, {nome_4=}')

print()
print('#' * 60 + ' Atribuindo o resto dos valores a uma única variável ' + '#' * 60)
print()

(pai, mae, *resto) = x

print(f'{pai=}, {mae=}, {resto=}')
