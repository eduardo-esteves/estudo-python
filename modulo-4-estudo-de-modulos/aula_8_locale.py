import calendar
import locale

from helper.print_msg_section import print_msg_section

# CPBA 280

# Imprime na tela a locale com o uso do Python, outra forma ainda
# melhor é o comando locale -a direto no sistema operacional
print(locale.getlocale())

# Após pegar o locale correto com getlocale() informo no segundo
# parâmetro, ou ainda poderia simplesmente passar uma string vazia
# assim pegaria o locale do sistema operacional por default.
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

print_msg_section('Imprime o calendário de Novembro comforme o locale')
# Imprime o calendário somente de novembro 2023
print(calendar.month(2023, 11))
