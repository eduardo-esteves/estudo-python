# Importo somente o módulo
import aula_39_packages.soma
# Importando a função especifica que está no meu package aula_39_packages/soma.py
from aula_39_packages.soma import soma
# Importo somente o modulo, mas como usei o "from" me facilita em criar um aliás
from aula_39_packages import soma as somar
# Importando um modulo com * (all) porém no modulo está sendo definido o
# que vai ser importado com __all__[]
from aula_39_packages.declaring_all import *

# Deixei por último a importação * (all) não recomendado
# from aula_39_packages.soma import *


# O jeito mais prático
result = soma(5, 5)
# Importar somente o modulo diretamente evita conflitos porém
# dá um pouquinho a mais de trabalho na manipulação, porém ainda é a opção mais segura.
result2 = somar.soma(10, 10)
# Importar somente o módulo teremos que manipular todo o namespace para acessar funcoes e variaveis.
result3 = aula_39_packages.soma.soma(20, 20)
# Só está acessível a função multiplicar do módulo declaring_all, isso por causa da
# diretiva __all__[] que foi definida, por exemplo não é possível acessar a var v_global
result4 = multiplicar(10, 2)

print(result4)
