# Aula 196
# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

# Os parametros que estão antes da barra devem ser obrigatoriamente posicionais
# e no caso de insistir em passar argumentos nomeados uma excessão será lançada
def subtrair(a, b, /):
    print(a - b)

# Neste exemplo tudo o que vier após o "*" deve ser obrigatoriamente nomeados
def soma(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(a + b + c)


soma(1, 2, c=3, nome='teste')
# subtrair(10, b=5)
