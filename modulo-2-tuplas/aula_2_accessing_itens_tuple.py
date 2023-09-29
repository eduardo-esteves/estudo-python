tupla = ("Gabriel", "Danny", "Arthur", "Danny")

item_1 = tupla[0]
print(item_1)

ultimo_item = tupla[-1]

# Podemos dizer me traga os valores a partir do item 2 até o item 5
# e mesmo que não haja essa quantidade, vai trazer até esse limite.
intervalo_itens = tupla[2:5]


# Ao emitir o primeiro elemento automaticamente vai pegar do
# primeiro até o próximo intervalo, como o último elemento
# é excluido então um truque é usar o método len() para dar
# a margem correta dos intervalos de todos os itens.
emitir_primeiro = tupla[:len(tupla)]

emitir_ultimo = tupla[1:]

print(intervalo_itens)
print(emitir_primeiro)
print(emitir_ultimo)

confirm_danny = 'Danny está na tupla' if 'Danny' in tupla else 'Danny não está na tupla'

print(confirm_danny)
