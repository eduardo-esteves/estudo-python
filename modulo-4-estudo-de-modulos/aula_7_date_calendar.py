import calendar

from helper.print_msg_section import print_msg_section

# CPBA 279

print_msg_section('Imprime o calendário de Novembro')
# Imprime o calendário somente de novembro 2023
print(calendar.month(2023, 11))

print_msg_section('Uma tupla com o primeiro e último dia do mês')
print(calendar.monthrange(2023,11))

print_msg_section('Tuplas com os dias numerados')
print(*tuple(enumerate(calendar.day_name)))

print_msg_section('Acessando o dia especifico')
print(calendar.day_name[2])
