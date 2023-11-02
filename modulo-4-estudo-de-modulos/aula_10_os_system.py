import os

from helper.print_msg_section import print_msg_section


# CPBA 282

caminho = os.path.join('/home/esteves', 'Downloads', 'ponto.pdf')
diretorio, arquivo = os.path.split(caminho)

print_msg_section('Imprimindo o caminho do arquivo')
print(caminho)

print_msg_section('Imprimindo o diretorio e nome do arquivo')
print(diretorio, arquivo, sep="\n")

print_msg_section('Verificando se o diretório ' + diretorio + ' existe')
exists = os.path.exists(diretorio)
print(exists)

print_msg_section('Obtendo o path do diretório corrente')
diretorio_atual = os.path.dirname(__file__)
print(diretorio_atual)
