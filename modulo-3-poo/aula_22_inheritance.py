from helper.print_msg_section import print_msg_section as print_msg

# 39
# Em versões anteriores ao Python 3 precisavamos passar object no
# constructor, porém a partir da versão 3 não é mais necessário.
class Pessoa(object):
    pass


# Depurando os metodos magicos que Pessoa herda da super classe object
eduardo = Pessoa
print(dir(eduardo))
