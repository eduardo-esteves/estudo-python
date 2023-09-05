# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
import sys
import sys as s
from sys import platform as pf, exit as finished
from sys import exit, platform
# Uma má pratica seria importar tudo do modulo
# from sys import *

# Preciso do namespace sys para usar um determinado módulo, vantagem não dá conflito com outras variáveis já definida
print(sys.platform)

# alias s - o modulo sys está sendo representado pelo objeto s
print(s.platform)

# Note que não preciso do namespace. Vantagens: nomes pequenos
print(platform)

# Podemos importar platform do módulo sys dando um apelido pf
print(pf)

exit()
finished()
