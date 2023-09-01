# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'upper'

# Executa o método upper() declarado na string se "metodo" for uma string vai ter o atributo upper()
nome = getattr(string, metodo)() if hasattr(string, metodo) else metodo

print(nome)

