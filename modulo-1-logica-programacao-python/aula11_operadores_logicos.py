entrada = input('[E]ntrar [S]air: ')
senha = input('Digite a senha: ')

db_senha = '123'

if ( (entrada == 'E' or entrada == 'e') and senha == db_senha):
    print('Usuario logado com sucesso!')
elif(entrada != 'E'):
    pass
else:
    print('Falha de autenticação')


nome = 'Edu'
#print(nome[0])

print(f'A letra E está no nome {nome} : ', 'E' in nome)
print(f'A letra E está no nome {nome} : ', 'E' not in nome)

print(not True)
