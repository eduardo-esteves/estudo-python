# Aula 179

# Modo não funcional, mais código e ainda não está funcionando
def recursive_funct(number, init=None):
    init = number if init is None else init
    total = number * init

    while init >= 1:
        init -= 1
        recursive_funct(init)

    return total


# Modo funcional menos código e funcionando perfeitamente
def recursive_funct_2(number):
    if number == 0:
        return 1
    else:
        return number * recursive_funct_2(number - 1)


fatorial_5 = recursive_funct_2(5)
print(fatorial_5)

